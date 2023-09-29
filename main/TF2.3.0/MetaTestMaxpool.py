import sys
sys.path.append(".")
from main.CONSTANT import *

import tensorflow as tf
import tensorflow.keras as K
from tensorflow.keras.layers import Input, MaxPool2D
from tensorflow.keras.models import Model, clone_model

import numpy as np
import h5py
import csv
import re
import constant
from utils import *






def SourceModel(shape):
    pool_size = np.random.randint(1, 5)
    strides = np.random.randint(1, 5)
    data_format = "channels_last" if FORMAT=="NHWC" else "channels_first"
    x = Input(shape=shape[1:])
    y = MaxPool2D(pool_size=(pool_size, pool_size), strides=(strides, strides),
                  padding="valid", data_format=data_format)(x)
    model = Model(x, y)
    return model


def maintest():
    OPERATOR = "Maxpool"
    TESTMODE = "metamorphosis"  # differential
    version = lib_version()

    shape = SHAPE
    # np.random.seed(0)
    data = generate_data(shape)

    # 保存文件到csv
    csv_path = os.path.join(MediTestRoot, "experiment/{}/{}/MetaResult_{}_{}_{}_{}.csv".
                            format(version, TESTMODE, version, FORMAT, DEVICE, OPERATOR))
    with open(file=csv_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Lib", "Format", "Device", "Operator", "MutaMode", "Dis", "Delta"])

        for muta_mode in range(0, 3):
            for i in range(100):
                source_model = SourceModel(shape)
                data = generate_data(shape)

                res = [version, FORMAT, DEVICE, OPERATOR]
                if muta_mode == 0:
                    # 输入系数
                    delta = np.random.uniform(0, DELTA, 1)[0]
                    source_result = source_model(data) * delta
                    follow_result = source_model(data * delta)
                    dis = norm_dis(source_result, follow_result)
                elif muta_mode == 1:
                    # 输入偏置
                    delta = np.random.uniform(-DELTA, DELTA, 1)[0]
                    source_result = source_model(data) + delta
                    follow_result = source_model(data + delta)
                    dis = norm_dis(source_result, follow_result)
                elif muta_mode == 2:
                    delta = 0
                    # 转置
                    if FORMAT == "NHWC":
                        source_result = tf.transpose(source_model(data), (0, 2, 1, 3))
                        follow_result = source_model(data.transpose(0, 2, 1, 3))
                    elif FORMAT == "NCHW":
                        source_result = tf.transpose(source_model(data), (0, 1, 3, 2))
                        follow_result = source_model(data.transpose(0, 1, 3, 2))
                    dis = norm_dis(source_result, follow_result)
                else:
                    break
                # 保存到csv
                res.append("MutaMode" + str(muta_mode))
                res.append(dis)
                res.append(delta)
                csv_writer.writerow(res)
                # 输出显示
                print("{};{};{};{};Iter:{};MutaMode:{};Dis:{};".format(version, OPERATOR, FORMAT, DEVICE, i, muta_mode,
                                                                       dis))


if __name__ == "__main__":
    maintest()
    print("end")
