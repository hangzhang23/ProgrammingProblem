    def _drop_item(target, duplex_list):
        """
        使用本方法需要将原本的特征列表self.feature_list进行重新包装，对一个行业的指标放在一个列表里。
        本方法的原理是对target的头一个特征挑出来，然后对新包装的特征列表进行条件遍历，在找到特征所在的
        行业后，对行业列表检查长度，在大于等于2的情况下进行剔除；如果行业列表等于1，查看j+1是否超出
        target长度，没有则j+=1（查找目标为target下一个特征），并且i也置为-1；超出则跳出外循环。如果没
        找到特征，则查看下一个行业。
        :param target: 列表形式表示所有小于baseline的特征（由小到大）
        :param duplex_list: 分行业的特征指标二维列表。
        :return: 剔除之后的二维列表。
        """
        try:
            i, j = 0, 0
            while i < len(duplex_list):
                for item in duplex_list[i]:
                    if target[j] == item:
                        if len(duplex_list[i]) == 1:
                            if j + 1 < len(target):
                                j += 1
                            else:
                                print('已经遍历所有target待选，没有找到可以删除的特征')
                                drop_item = None
                                raise StopIteration
                            i = -1
                            break
                        elif len(duplex_list[i]) <= 0:
                            raise ValueError('本area全空，请检查原本特征集')
                        else:
                            duplex_list[i].remove(item)
                            drop_item = item
                            raise StopIteration
                    else:
                        continue
                i += 1
        except StopIteration:
            pass
        return duplex_list, drop_item
