from django.db import models


class Manufacturer(models.Model):
    """
    制造商，品牌
    """
    name = models.CharField(max_length=10, unique=True, verbose_name="制造商品牌")
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class AssetModel(models.Model):
    """
    设备型号
    """
    name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, unique=True)
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class ResourceType(models.Model):
    """
    资源类型
    """
    type = models.CharField(max_length=10, unique=True, verbose_name="资源类型")
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    class Meta:
        ordering = ('-type',)

    def __str__(self):
        return self.type


class Company(models.Model):
    """
    公司
    """
    name = models.CharField(max_length=10, unique=True, verbose_name="公司")
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class MaintenanceCompany(models.Model):
    """
    维保厂家
    """
    company_name = models.CharField(max_length=20, unique=True, verbose_name="维保公司")
    person_number = models.CharField(max_length=50, blank=True, verbose_name="联系人及电话")

    class Meta:
        ordering = ('-company_name',)

    def __str__(self):
        return self.company_name


class Business(models.Model):
    """
    业务线
    """
    pass


class Memory(models.Model):
    """
    内存
    """
    model_choice = ((1, 'DDR3'), (2, 'DDR4'), (3, 'DDR5'),)
    unit_choice = ((1, 'GB'), (2, "TB"), (3, 'PB'),)
    model = models.CharField(choices=model_choice, default=1, verbose_name="内存型号")
    size = models.IntegerField(max_length=3, default=8, verbose_name="内存容量")
    unit = models.IntegerField(max_length=2, default=1, verbose_name="单位")
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    def __str__(self):
        return self.size


class NetworkCard(models.Model):
    """
    网卡，每台主机有多块网卡，多个IP
    """
    name = models.CharField(max_length=10, verbose_name="网卡名")
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    def __str__(self):
        return self.name


class Cpu(models.Model):
    """
    CPU，一台主机可以有多个CPU
    """
    name = models.CharField(max_length=30, verbose_name="cpu型号")
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    def __str__(self):
        return self.name


class Ipaddress(models.Model):
    """
    IP地址，与网卡绑定
    """
    network_device = models.ForeignKey(NetworkCard, on_delete=models.CASCADE, verbose_name="网卡绑定")
    address = models.IPAddressField(verbose_name="IP地址")
    vip = models.IPAddressField(blank=True, verbose_name="VIP地址")
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    def __str__(self):
        return self.address


class Disk(models.Model):
    """
    硬盘
    """
    unit_choice = ((1, 'GB'), (2, "TB"), (3, 'PB'),)
    size = models.IntegerField(max_length=5, verbose_name="磁盘容量")
    unit = models.IntegerField(max_length=1, choices=unit_choice, verbose_name="单位")
    sn = models.CharField(max_length=20, unique=True, verbose_name="磁盘SN")
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    def __str__(self):
        return self.size


class Raid(models.Model):
    """
    raid信息
    """
    raid_model = models.CharField(max_length=10, verbose_name='raid信息')
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    def __str__(self):
        return self.raid_model


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

    def __str__(self):
        return self.asset_id


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
    raid_type = models.ForeignKey(Raid, on_delete=models.CASCADE, verbose_name="Raid信息")
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE, verbose_name='CPU')
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, verbose_name="内存")
    manage_ip = models.IPAddressField(unique=True, verbose_name="管理卡IP")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    remark = models.CharField(max_length=100, verbose_name="备注")

    def __str__(self):
        return self.asset_id


class Server(models.Model):
    """
    服务器表
    """
    host_name = models.CharField(max_length=20, unique=True, verbose_name="主机名")
    # 服务器类型填写【虚拟机，物理机】
    server_type_choice = ((1, "物理机"), (2, "虚拟机"),)
    server_type = models.CharField(choices=server_type_choice, verbose_name="服务器类型")
    os_system = models.CharField(max_length=10, verbose_name="操作系统")
    ipaddr = models.IPAddressField(unique=True, verbose_name="IP地址")
    disk = models.IntegerField(max_length=10, verbose_name="硬盘")
    cpu = models.IntegerField(max_length=2, verbose_name='CPU核数')
    memory = models.IntegerField(max_length=3, verbose_name="内存")

    def __str__(self):
        return self.host_name


class InternetAsset(models.Model):
    """
    网络设备
    """
    host_name = models.CharField(max_length=20, unique=True, verbose_name="主机名")
    ipaddr = models.IPAddressField(unique=True, verbose_name="IP地址")


class Status(models.Model):
    """
    资产状态表
    """
    pass




