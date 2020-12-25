#!/usr/bin/env python
# coding=utf-8
import json
import time
import traceback
from multiprocessing.pool import ThreadPool

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException, ServerException
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceNetworkSpecRequest import ModifyInstanceNetworkSpecRequest

CHECK_MODIFY_TIMEOUT = 60
CHECK_MODIFY_TIME_INTERVAL = 2


class InvalidParameterError(Exception):
    pass


class TimeoutError(Exception):
    pass


class AliyunModifyInstanceNetworkSpecExample(object):

    def __init__(self):
        self.access_id = '<ACCESS_KEY_ID>'
        self.access_secret = '<ACCESS_SECRET>'
        # 实例所属的地域ID
        self.region_id = 'cn-zhangjiakou'
        # 需要带宽配置的实例ID
        self.instance_ids = ['i-8vbj4hcssgvnai78h063']
        # 公网出带宽最大值，单位为Mbps（Megabit per second）。取值范围：[0, 100]
        self.internet_max_bandwidth_out = 10
        # 转换网络计费方式。取值范围：PayByBandwidth：按固定带宽计费；PayByTraffic：按使用流量计费
        self.network_charge_type = 'PayByTraffic'

        # 是否自动支付，如果设为false，会生成正常的未支付订单，可以登录ECS管理控制台支付
        self.auto_pay = True

        self.client = AcsClient(self.access_id, self.access_secret, self.region_id)
        self.pool = ThreadPool(100)

    def run(self):
        try:
            self.check_instance_ids()
            self.modify_instance_network_specs()
            self.check_modify_results()
        except ClientException as e:
            print('Fail. Something with your connection with Aliyun go incorrect.'
                  ' Code: {code}, Message: {msg}'
                  .format(code=e.error_code, msg=e.message))
        except ServerException as e:
            print('Fail. Business error.'
                  ' RequestId: {request_id}, Code: {code}, Message: {msg}'
                  .format(request_id=e.request_id, code=e.error_code, msg=e.message))
        except InvalidParameterError as e:
            print(e.message)
        except Exception:
            print('Unhandled error')
            print(traceback.format_exc())

    def check_instance_ids(self):
        """
        检查实例ID的有效性
        """
        print('Check instance ids')
        instances = self.describe_instances()
        instance_ids = [instance['InstanceId'] for instance in instances]
        invalid_instance_ids = set(self.instance_ids) - set(instance_ids)
        if invalid_instance_ids:
            msg = 'Invalid instance ids: {}'.format(invalid_instance_ids)
            raise InvalidParameterError(msg)

    def describe_instances(self, instance_ids=None):
        """
        描述实例
        :param instance_ids: 实例ID列表
        :return: 实例信息列表
        """
        instances = []
        page_size = 10
        page_number = 1
        total_count = None

        request = DescribeInstancesRequest()
        request.set_InstanceIds(json.dumps(instance_ids or self.instance_ids))
        request.set_PageNumber(page_number)
        request.set_PageSize(page_size)

        while total_count is None or page_number * page_size < total_count:
            body = self.client.do_action_with_exception(request)
            data = json.loads(body)
            instances.extend(data['Instances']['Instance'])
            total_count = data['TotalCount']
            page_number += 1
            request.set_PageNumber(page_number)

        return instances

    def modify_instance_network_specs(self):
        """
        批量修改实例带宽
        :return:
        """
        print('modify instance network specs')
        self.pool.map(self.modify_instance_network_spec, self.instance_ids)

    def modify_instance_network_spec(self, instance_id):
        """
        修改实例带宽
        :param instance_id: 实例ID
        :return:
        """
        print('Modify instance {} network spec'.format(instance_id))
        request = ModifyInstanceNetworkSpecRequest()
        request.set_InstanceId(instance_id)
        request.set_AutoPay(self.auto_pay)
        request.set_NetworkChargeType(self.network_charge_type)
        request.set_InternetMaxBandwidthOut(self.internet_max_bandwidth_out)

        self.client.do_action_with_exception(request)

    def check_modify_results(self):
        """
        验证带宽是否修改成功
        :return:
        """
        print('Check modify result')
        start = time.time()
        instance_ids = list(self.instance_ids)
        while not instance_ids:
            instances = self.describe_instances(instance_ids)
            for instance in instances:
                if instance['InternetChargeType'] == self.network_charge_type and \
                        instance['InternetMaxBandwidthOut'] == self.internet_max_bandwidth_out:
                    instance_ids.remove(instance['InstanceId'])

            if time.time() - start > CHECK_MODIFY_TIMEOUT:
                msg = 'Check modify instance network spec timeout. ' \
                      'Because it takes too much time, View the result detail: {}' \
                    .format(instance_ids)
                raise TimeoutError(msg)

            time.sleep(CHECK_MODIFY_TIME_INTERVAL)

        print('Successful, all of the instances modified network spec successfully')


if __name__ == '__main__':
    AliyunModifyInstanceNetworkSpecExample().run()