from abc import ABCMeta

from pure_object_oriented.SingletonMeta import SingletonMeta


class ABCAndSingletonMeta(ABCMeta, SingletonMeta):
    pass
