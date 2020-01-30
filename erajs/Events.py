import enum


class SystemEvent(enum.Enum):
    """
    # 事件枚举
    - ENGINE_INIT_STARTED
        - 引擎初始化（由MID触发）
    - FILE_SYSTEM_CHECKED
        - 文件系统完整性检查完成（由DataManager: check_file_system触发）
    - ENGINE_CONFIG_LOADED
        - 引擎配置文件加载完成（由DataManager: load_config触发）
    - PLUGIN_FOUND
        - 扫描到一个插件（由ModuleManager触发）
    - PLUGINS_SCAN_FINISHED
        - 插件扫描完成（由ModuleManager触发）
    - PLUGIN_LOADED
        - 加载完一个插件（由ModuleManager触发）
    - PLUGINS_LOAD_FINISHED
        - 插件加载完成（由ModuleManager触发）
    - SERVER_CONNECTED
        - 引擎配置文件加载完成（由DataManager: load_config触发）
    - SERVER_CONFIG_SENT
        - 引擎配置文件加载完成（由DataManager: load_config触发）
    - DATA_FILE_FOUND
        - 扫描到一个数据文件（由DataManager触发）
    - DATA_FILES_SCAN_FINISHED
        - 数据文件扫描完成（由DataManager触发）
    - DATA_FILE_LOADED
        - 加载完一个数据文件（由DataManager触发）
    - DATA_FILES_LOAD_FINISHED
        - 数据文件加载完成（由DataManager触发）
    - SCRIPT_FOUND
        - 扫描到一个脚本（由ModuleManager触发）
    - SCRIPTS_SCAN_FINISHED
        - 脚本扫描完成（由ModuleManager触发）
    - SCRIPT_LOADED
        - 加载完一个脚本（由ModuleManager触发）
    - SCRIPTS_LOAD_FINISHED
        - 脚本加载完成（由ModuleManager触发）
    - DLC_FOUND
        - 扫描到一个DLC（由ModuleManager触发）
    - DLCS_SCAN_FINISHED
        - DLC扫描完成（由ModuleManager触发）
    - DLC_LOADED
        - 加载完一个DLC（由ModuleManager触发）
    - DLCS_LOAD_FINISHED
        - DLC加载完成（由ModuleManager触发）
    - MOD_FOUND
        - 扫描到一个MOD（由ModuleManager触发）
    - MODS_SCAN_FINISHED
        - MOD扫描完成（由ModuleManager触发）
    - MOD_LOADED
        - 加载完一个MOD（由ModuleManager触发）
    - MODS_LOAD_FINISHED
        - MOD加载完成（由ModuleManager触发）
    - ENGINE_INIT_FINISHED_SIGNAL_SENT
        - 引擎初始化信号发出（由NetManager触发）
    - ENGINE_INIT_FINISHED
        - 引擎初始化完成（由Engine触发）
    """
    ENGINE_INIT_STARTED = enum.auto()
    FILE_SYSTEM_CHECKED = enum.auto()
    ENGINE_CONFIG_LOADED = enum.auto()
    PLUGIN_FOUND = enum.auto()
    PLUGINS_SCAN_FINISHED = enum.auto()
    PLUGIN_LOADED = enum.auto()
    PLUGINS_LOAD_FINISHED = enum.auto()
    SERVER_CONNECTED = enum.auto()
    SERVER_CONFIG_SENT = enum.auto()
    DATA_FILE_FOUND = enum.auto()
    DATA_FILES_SCAN_FINISHED = enum.auto()
    DATA_FILE_LOADED = enum.auto()
    DATA_FILES_LOAD_FINISHED = enum.auto()
    SCRIPT_FOUND = enum.auto()
    SCRIPTS_SCAN_FINISHED = enum.auto()
    SCRIPT_LOADED = enum.auto()
    SCRIPTS_LOAD_FINISHED = enum.auto()
    DLC_FOUND = enum.auto()
    DLCS_SCAN_FINISHED = enum.auto()
    DLC_LOADED = enum.auto()
    DLCS_LOAD_FINISHED = enum.auto()
    MOD_FOUND = enum.auto()
    MODS_SCAN_FINISHED = enum.auto()
    MOD_LOADED = enum.auto()
    MODS_LOAD_FINISHED = enum.auto()
    ENGINE_INIT_FINISHED_SIGNAL_SENT = enum.auto()
    ENGINE_INIT_FINISHED = enum.auto()
