from django.db import models


class Manufacturer(models.Model):
    """
    制造商，品牌
    """
    name = models.CharField(max_length=10, unique=True, verbose_name="制造商品牌")

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class AssetModel(models.Model):
    """
    设备型号
    """
    name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, unique=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class ResourceType(models.Model):
    """
    资源类型
    """
    type = models.CharField(max_length=10, unique=True, verbose_name="资源类型")

    class Meta:
        ordering = ('-type',)

    def __str__(self):
        return self.type


class Company(models.Model):
    """
    公司
    """
    name = models.CharField(max_length=10, unique=True, verbose_name="公司")

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Contract(models.Model):
    """
    合同，维保
    """
    pass


class Business(models.Model):
    """
    业务线
    """
    pass


class Memory(models.Model):
    """
    内存
    """
    pass


class NetworkCard(models.Model):
    """
    网卡，每台主机有多块网卡，多个IP
    """
    pass


class Ipaddress(models.Model):
    """
    IP地址，与网卡绑定
    """
    pass


class Disk(models.Model):
    """
    硬盘
    """
    pass


class Assets(models.Model):
    """
    资产表
    """
    asset_id = models.CharField(max_length=30, unique=True, verbose_name="资产编号")
    asset_model = models.ForeignKey(to=AssetModel, on_delete=models.CASCADE, verbose_name="设备型号")
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.CASCADE, verbose_name="设备品牌")
    asset_type = models.ForeignKey(to=ResourceType, on_delete=models.CASCADE, verbose_name="设备类型")
    owner = models.ForeignKey(to=Company, on_delete=models.CASCADE, verbose_name="所属者")
    use = models.ForeignKey(to=Company, on_delete=models.CASCADE, verbose_name="使用者")
    sn = models.CharField(max_length=50, unique=True, verbose_name="设备SN")
    contract = models.OneToOneField(to=Contract, on_delete=models.CASCADE, verbose_name="维保信息")
    buy_time = models.DateField(verbose_name="购买时间", default="2000-01-01")
    # business = models.ForeignKey(Business, on_delete=models.CASCADE, verbose_name="所属业务线")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    remark = models.CharField(max_length=100, verbose_name="备注")


class ServerAsset(models.Model):
    """
    服务器资产表
    """
    # 服务器类型填写【虚拟机，物理机】
    server_type = models.CharField(max_length=10, unique=True, verbose_name="服务器类型")
    os_system = models.CharField(max_length=10, verbose_name="操作系统")
    # 资产ID，一一对应资产表
    asset_id = models.OneToOneField(Assets, on_delete=models.CASCADE, verbose_name="资产ID")
    # business = models.ForeignKey(Business, on_delete=models.CASCADE, verbose_name="所属业务线")
    network_device = models.ForeignKey(NetworkCard, on_delete=models.CASCADE, verbose_name="网卡")
    disk_device = models.ForeignKey(Disk, on_delete=models.CASCADE, verbose_name="硬盘")
    cpu = models.CharField(max_length=30, verbose_name='CPU')
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, verbose_name="内存")
    manage_ip = models.IPAddressField(unique=True, verbose_name="管理卡IP")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    remark = models.CharField(max_length=100, verbose_name="备注")


class Server(models.Model):
    """
    服务器表
    """
    # 服务器类型填写【虚拟机，物理机】
    server_type = models.CharField(max_length=10, unique=True, verbose_name="服务器类型")
    os_system = models.CharField(max_length=10, verbose_name="操作系统")


class InternetAsset(models.Model):
    """
    网络设备
    """
    pass


class Status(models.Model):
    """
    资产状态表
    """
    pass


class Application(models.Model):
    """
    应用表
    """
    pass


