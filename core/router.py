from rest_framework.routers import DefaultRouter


class SingletonClass(DefaultRouter):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance

router = SingletonClass()
