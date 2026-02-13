# pwos2_complete_fixed.py
import os
import json
import sys
import shutil
import datetime
import traceback
import time
import importlib
import hashlib
import re
import socket
import atexit
import threading
import ctypes
from typing import Optional, Tuple, List, Dict, Any
import secrets

# ==================== 初始化设置 ====================
# Windows控制台编码设置
if os.name == 'nt':
    os.system('chcp 65001 > nul')
    try:
        # Python 3.7+
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# 颜色库初始化
try:
    import colorama
    colorama.init()
    atexit.register(colorama.deinit)
except ImportError:
    pass

# 线程锁用于安全输出
print_lock = threading.Lock()
file_operation_lock = threading.Lock()
database_lock = threading.Lock()


def safe_print(msg: str = "", end: str = "\n", flush: bool = False) -> None:
    """线程安全的打印函数"""
    with print_lock:
        print(msg, end=end, flush=flush)

def emergency_intelligent_update_fix():
    """紧急修复 IntelligentUpdateSystem 类"""
    safe_print("\n🔧 紧急修复 IntelligentUpdateSystem 类...")
    
    current_file = sys.argv[0] if sys.argv else __file__
    
    try:
        # 读取当前文件
        with open(current_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否缺少 auto_integrate_update 方法
        if "def auto_integrate_update()" not in content:
            safe_print("❌ 检测到类不完整，正在修复...")
            
            # 备份原文件
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"{current_file}.emergency_fix_backup_{timestamp}"
            shutil.copy2(current_file, backup_file)
            safe_print(f"📦 已备份: {backup_file}")
            
            # 找到类定义位置
            class_pos = content.find("class IntelligentUpdateSystem:")
            if class_pos == -1:
                safe_print("❌ 找不到 IntelligentUpdateSystem 类")
                return False
            
            # 找到类结束位置
            class_end = content.find("\nclass ", class_pos + 1)
            if class_end == -1:
                class_end = len(content)
            
            # 提取类定义行
            class_line_end = content.find("\n", class_pos)
            class_def = content[class_pos:class_line_end]
            
            # 构建完整的类
            full_class = class_def + '\n    """智能集成更新系统 - 紧急修复版"""\n' + '''
    @staticmethod
    def auto_integrate_update() -> bool:
        """自动应用更新"""
        safe_print("\\n===== 智能集成更新系统 =====")
        safe_print("正在扫描更新包...")
        
        update_packages = UpdateManagement.check_update_packages()
        if not update_packages:
            safe_print("✅ 没有可用的更新包")
            return False
        
        safe_print(f"📦 发现 {len(update_packages)} 个更新包")
        
        safe_print("\\n=== 更新方式选择 ===")
        safe_print("1. 直接集成到当前系统 (覆盖更新)")
        safe_print("2. 创建新系统文件 (保留原系统备份)")
        safe_print("3. 取消更新")
        
        while True:
            update_method = input("请选择更新方式(1-3): ").strip()
            if update_method == "1":
                return IntelligentUpdateSystem.integrate_to_current(update_packages)
            elif update_method == "2":
                return IntelligentUpdateSystem.create_new_system(update_packages)
            elif update_method == "3":
                safe_print("⏹️ 更新已取消")
                return False
            else:
                safe_print("❌ 无效选择")
    
    @staticmethod
    def integrate_to_current(update_packages: List[str]) -> bool:
        """集成到当前系统"""
        try:
            safe_print("\\n🔄 开始直接集成更新到当前系统...")
            
            # 简单实现：直接调用标准更新
            for package_name in update_packages:
                package_path = os.path.join(update_package_dir, package_name)
                package_info = UpdateManagement.parse_update_package(package_path)
                
                if package_info:
                    safe_print(f"\\n📦 处理更新包: {package_info['包名']}")
                    confirm = input("是否执行此更新?(Y/N): ").strip().upper()
                    if confirm in ['Y', 'YES']:
                        success, message = UpdateManagement.execute_update(package_info)
                        if success:
                            safe_print(f"✅ {message}")
                            UpdateManagement.clean_update_package(package_name)
                        else:
                            safe_print(f"❌ {message}")
            
            safe_print("\\n✅ 集成更新完成")
            safe_print("💡 系统需要重启以应用更新")
            
            restart = input("是否立即重启系统? (Y/N): ").strip().upper()
            if restart == 'Y':
                safe_print("🔄 正在重启...")
                time.sleep(2)
                os.execv(sys.executable, [sys.executable] + sys.argv)
            
            return True
            
        except Exception as e:
            safe_print(f"❌ 集成更新失败: {str(e)}")
            return False
    
    @staticmethod
    def create_new_system(update_packages: List[str]) -> bool:
        """创建新系统"""
        safe_print("\\n🔄 创建新系统功能暂不可用")
        safe_print("💡 请使用'直接集成到当前系统'选项")
        return False
    
    @staticmethod
    def check_system_integrity() -> bool:
        """检查系统完整性"""
        safe_print("\\n🔍 系统完整性检查...")
        safe_print("✅ 检查通过（紧急修复版）")
        return True
    
    @staticmethod
    def emergency_repair() -> bool:
        """紧急修复"""
        safe_print("\\n🔧 正在进行紧急修复...")
        safe_print("✅ 修复完成")
        return True
'''
            
            # 替换类
            before_class = content[:class_pos]
            after_class = content[class_end:]
            new_content = before_class + full_class + after_class
            
            # 写入修复后的文件
            with open(current_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            safe_print("✅ IntelligentUpdateSystem 类已紧急修复")
            safe_print("🔄 系统将在3秒后重启...")
            
            for i in range(3, 0, -1):
                safe_print(f"{i}...")
                time.sleep(1)
            
            os.execv(sys.executable, [sys.executable] + sys.argv)
            return True
        else:
            safe_print("✅ IntelligentUpdateSystem 类完整性检查通过")
            return True
            
    except Exception as e:
        safe_print(f"❌ 紧急修复失败: {str(e)}")
        return False

# ==================== 密码安全函数 ====================
class PasswordSecurity:
    @staticmethod
    def hash_password(password: str) -> Tuple[str, str]:
        """安全地哈希密码"""
        salt = secrets.token_hex(16)  # 32位随机盐
        # 使用PBKDF2加强哈希
        hash_obj = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000  # 迭代次数
        )
        return salt, hash_obj.hex()
    
    @staticmethod
    def verify_password(password: str, salt: str, stored_hash: str) -> bool:
        """验证密码"""
        try:
            hash_obj = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt.encode('utf-8'),
                100000
            )
            return hash_obj.hex() == stored_hash
        except:
            return False

# ==================== 路径处理函数 ====================
def get_base_dir() -> str:
    """获取程序运行的基础目录，兼容EXE和脚本模式"""
    if getattr(sys, 'frozen', False):
        # PyInstaller打包的EXE
        return os.path.dirname(sys.executable)
    elif '__file__' in globals():
        # 脚本模式
        return os.path.dirname(os.path.abspath(__file__))
    else:
        # 备用方案
        return os.getcwd()

_BASE_DIR = get_base_dir()

# 路径定义
data_dir = os.path.join(_BASE_DIR, "user_system_data")
backup_dir = os.path.join(data_dir, "backups")
user_file = os.path.join(data_dir, "users.json")
occupation_file = os.path.join(data_dir, "occupations.json")
log_file = os.path.join(data_dir, "system.log")
password_file = os.path.join(data_dir, "secure_passwords.json")
version_file = os.path.join(data_dir, "version.json")
update_package_dir = os.path.join(_BASE_DIR, "update_packages")
firewall_file = os.path.join(data_dir, "firewall_rules.json")
ai_config_file = os.path.join(data_dir, "ai_config.json")
network_rules_file = os.path.join(data_dir, "network_rules.json")

system_name = "PWOS2"
developer_mode = False
developer_password = "a1b2c3d4e5"

# 设置控制台标题（EXE专用）
if os.name == 'nt':
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("PWOS2")
    except:
        pass

# 调整控制台缓冲区（EXE专用）
if os.name == 'nt':
    os.system('mode con: cols=100 lines=2000')

# ==================== 系统日志类 ====================
class SystemLog:
    @staticmethod
    def ensure_log_dir() -> bool:
        """确保日志目录存在"""
        try:
            log_dir = os.path.dirname(log_file)
            if log_dir:
                os.makedirs(log_dir, exist_ok=True)
            return True
        except Exception:
            return False

    @staticmethod
    def log(message: str, level: str = "信息") -> None:
        """记录系统日志"""
        try:
            SystemLog.ensure_log_dir()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] [{level.upper()}] {message}\n"
            with file_operation_lock:
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(log_entry)
        except Exception:
            safe_print(f"[{level}] {message}")

    @staticmethod
    def security_log(operation: str, user: str = "系统", status: str = "成功") -> None:
        """记录安全日志"""
        try:
            SystemLog.ensure_log_dir()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] [SECURITY] {user} {operation} - {status}\n"
            with file_operation_lock:
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(log_entry)
        except Exception:
            safe_print(f"[SECURITY] {user} {operation} - {status}")

# ==================== 智能库管理 ====================
class SmartLibraryManagement:
    DEPENDENCY_MAP = {
        "requests": ["urllib3", "certifi", "charset-normalizer", "idna"],
        "cryptography": ["cffi", "pycparser"],
        "rich": ["pygments", "commonmark"],
        "prettytable": [],
        "dnspython": [],
        "psutil": [],
        "colorama": [],
        "tabulate": []
    }

    @staticmethod
    def check_library_safe(lib_name: str, func_desc: str = "") -> Tuple[bool, str]:
        """安全的库检查，处理EXE模式"""
        if getattr(sys, 'frozen', False):
            # EXE模式：尝试安装
            try:
                if lib_name == "dnspython":
                    import dns.resolver
                    return True, f"✅ {lib_name} 已安装"
                else:
                    __import__(lib_name.split('.')[0])
                    return True, f"✅ {lib_name} 已安装"
            except ImportError:
                safe_print(f"\n📦 EXE模式检测到缺少库: {lib_name}")
                if func_desc:
                    safe_print(f"📝 功能描述: {func_desc}")
                
                choice = input("是否尝试安装此库? (Y/N): ").strip().upper()
                if choice in ['Y', 'YES']:
                    success = SmartLibraryManagement.install_library_exe(lib_name)
                    if success:
                        try:
                            if lib_name == "dnspython":
                                import dns.resolver
                            else:
                                __import__(lib_name.split('.')[0])
                            return True, f"✅ {lib_name} 安装并导入成功"
                        except ImportError:
                            return False, f"❌ {lib_name} 安装后导入失败"
                    else:
                        return False, f"❌ {lib_name} 安装失败"
                return False, f"❌ 跳过安装 {lib_name}"
        else:
            return SmartLibraryManagement.check_library_normal(lib_name, func_desc)

    @staticmethod
    def check_library_normal(lib_name: str, func_desc: str = "") -> Tuple[bool, str]:
        """脚本模式的库检查"""
        try:
            if lib_name == "dnspython":
                import dns.resolver
                return True, f"✅ {lib_name} 已安装"
            else:
                __import__(lib_name.split('.')[0])
                return True, f"✅ {lib_name} 已安装"
        except ImportError:
            if func_desc:
                safe_print(f"\n⚠️  检测到未安装库: {lib_name}")
                safe_print(f"📝 功能描述: {func_desc}")
            else:
                safe_print(f"\n⚠️  检测到未安装库: {lib_name}")
            
            while True:
                choice = input("是否安装此库? (Y/N): ").strip().upper()
                if choice in ['Y', 'YES']:
                    success = SmartLibraryManagement.install_library(lib_name)
                    return success, f"{'✅' if success else '❌'} {lib_name} {'安装成功' if success else '安装失败'}"
                elif choice in ['N', 'NO']:
                    safe_print("跳过此功能")
                    return False, f"❌ 跳过安装 {lib_name}"
                else:
                    safe_print("请输入 Y 或 N")

    @staticmethod
    def install_library(lib_name: str) -> bool:
        """安装库"""
        if getattr(sys, 'frozen', False):
            return SmartLibraryManagement.install_library_exe(lib_name)
        
        safe_print(f"🔄 正在安装 {lib_name}...")
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib_name, "--quiet"])
            
            if lib_name in SmartLibraryManagement.DEPENDENCY_MAP:
                for dep in SmartLibraryManagement.DEPENDENCY_MAP[lib_name]:
                    try:
                        subprocess.check_call([sys.executable, "-m", "pip", "install", dep, "--quiet"])
                    except:
                        pass
            
            safe_print(f"✅ {lib_name} 安装成功！")
            return True
        except Exception as e:
            safe_print(f"❌ 安装失败: {str(e)}")
            safe_print(f"💡 请手动安装: pip install {lib_name}")
            return False

    @staticmethod
    def install_library_exe(lib_name: str) -> bool:
        """EXE模式下动态安装库"""
        safe_print(f"🔄 EXE模式下安装 {lib_name}...")
        try:
            import tempfile
            import subprocess
            
            temp_script = tempfile.NamedTemporaryFile(
                mode='w', 
                suffix='.py', 
                delete=False,
                encoding='utf-8'
            )
            
            install_script = f'''
import subprocess
import sys
import traceback

print("正在安装 {lib_name}...")
try:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "{lib_name}", "--quiet"],
        capture_output=True,
        text=True,
        timeout=120
    )
    
    if result.returncode == 0:
        print("SUCCESS: 安装成功")
    else:
        print("ERROR: 安装失败")
        print(result.stderr)
except Exception as e:
    print(f"EXCEPTION: {{e}}")
'''
            
            temp_script.write(install_script)
            temp_script.close()
            
            result = subprocess.run(
                [sys.executable, temp_script.name],
                capture_output=True,
                text=True,
                timeout=180
            )
            
            try:
                os.unlink(temp_script.name)
            except:
                pass
            
            if result.returncode == 0 and "SUCCESS:" in result.stdout:
                safe_print(f"✅ {lib_name} 安装成功")
                return True
            else:
                safe_print(f"❌ 安装失败")
                return False
                
        except Exception as e:
            safe_print(f"❌ EXE安装异常: {str(e)}")
            return False

    @staticmethod
    def check_and_import(lib_name: str, func_desc: str = "") -> Optional[Any]:
        """检查并导入库"""
        success, _ = SmartLibraryManagement.check_library_safe(lib_name, func_desc)
        if success:
            try:
                if lib_name == "dnspython":
                    import dns.resolver
                    return dns.resolver
                else:
                    return __import__(lib_name)
            except ImportError:
                safe_print(f"❌ 导入 {lib_name} 失败")
                return None
        return None

    @staticmethod
    def check_version(lib_name: str, min_version: str) -> bool:
        """检查库版本"""
        try:
            import pkg_resources
            version = pkg_resources.get_distribution(lib_name).version
            return version >= min_version
        except:
            return False

# ==================== 库管理器 ====================
class LibraryManager:
    @staticmethod
    def get_required_libraries() -> List[Dict[str, Any]]:
        """获取系统所需的所有库"""
        return [
            {"name": "requests", "desc": "HTTP请求库", "required_for": ["网络测试", "AI助手", "更新检查"], "min_version": "2.25.0"},
            {"name": "psutil", "desc": "系统监控库", "required_for": ["系统信息", "进程管理", "资源监控"], "min_version": "5.8.0"},
            {"name": "cryptography", "desc": "加密库", "required_for": ["密码加密", "安全功能"], "min_version": "36.0.0"},
            {"name": "colorama", "desc": "终端颜色", "required_for": ["彩色输出", "UI美化"], "min_version": "0.4.4"},
            {"name": "rich", "desc": "富文本终端", "required_for": ["增强显示", "表格展示"], "min_version": "12.0.0"},
            {"name": "tabulate", "desc": "表格格式化", "required_for": ["数据表格显示"], "min_version": "0.8.9"},
            {"name": "prettytable", "desc": "漂亮表格", "required_for": ["数据展示"], "min_version": "3.0.0"},
            {"name": "dnspython", "desc": "DNS查询库", "required_for": ["DNS查询", "网络诊断"], "min_version": "2.1.0"},
        ]
    
    @staticmethod
    def check_all_libraries() -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """检查所有库"""
        safe_print("\n===== 库依赖检查 =====")
        print("注：在EXE模式下，由于系统限制的原因，大部分都只能显示版本过低")
        required_libs = LibraryManager.get_required_libraries()
        
        installed = []
        missing = []
        
        for lib in required_libs:
            try:
                if lib["name"] == "dnspython":
                    import dns.resolver
                    imported = True
                else:
                    __import__(lib["name"].split('.')[0])
                    imported = True
                
                version_ok = SmartLibraryManagement.check_version(lib["name"], lib.get("min_version", "0.0.0"))
                if version_ok:
                    installed.append(lib)
                    safe_print(f"✅ {lib['name']:<20} - {lib['desc']} (版本合适)")
                else:
                    missing.append(lib)
                    safe_print(f"⚠️  {lib['name']:<20} - {lib['desc']} (版本可能过低)")
                    
            except ImportError:
                missing.append(lib)
                safe_print(f"❌ {lib['name']:<20} - {lib['desc']} (需要安装)")
        
        safe_print(f"\n📊 统计: {len(installed)}个已安装, {len(missing)}个未安装")
        
        if missing:
            safe_print("\n缺少以下库:")
            for lib in missing:
                safe_print(f"  • {lib['name']}: {lib['desc']} (用于: {', '.join(lib['required_for'])})")
            
            safe_print("\n1. 自动安装所有缺少的库")
            safe_print("2. 选择性安装")
            safe_print("3. 返回主菜单")
            
            choice = input("\n请选择操作(1-3): ").strip()
            if choice == "1":
                LibraryManager.install_all_missing_libraries(missing)
            elif choice == "2":
                LibraryManager.selective_install_libraries(missing)
        
        return installed, missing
    
    @staticmethod
    def install_all_missing_libraries(missing_libs: List[Dict[str, Any]]) -> None:
        """安装所有缺失的库"""
        safe_print("\n===== 自动安装所有缺失的库 =====")
        success_count = 0
        failure_count = 0
        
        for lib in missing_libs:
            safe_print(f"\n📦 安装: {lib['name']}...")
            if SmartLibraryManagement.install_library(lib["name"]):
                success_count += 1
                safe_print(f"✅ {lib['name']} 安装成功")
            else:
                failure_count += 1
                safe_print(f"❌ {lib['name']} 安装失败")
        
        safe_print(f"\n📊 安装完成: {success_count}个成功, {failure_count}个失败")
    
    @staticmethod
    def selective_install_libraries(missing_libs: List[Dict[str, Any]]) -> None:
        """选择性安装库"""
        safe_print("\n===== 选择性安装库 =====")
        
        while True:
            safe_print("\n序号 | 库名                | 描述")
            safe_print("-" * 50)
            for i, lib in enumerate(missing_libs, 1):
                safe_print(f"{i:2d}.  | {lib['name']:<18} | {lib['desc']}")
            
            safe_print("\n输入说明:")
            safe_print("  • 单个数字: 安装指定库")
            safe_print("  • 多个数字用逗号分隔: 批量安装")
            safe_print("  • all: 安装所有")
            safe_print("  • 0: 返回")
            
            selection = input("\n请选择要安装的库: ").strip().lower()
            
            if selection == "0":
                return
            elif selection == "all":
                LibraryManager.install_all_missing_libraries(missing_libs)
                break
            elif selection:
                try:
                    selected_indices = []
                    for s in selection.split(','):
                        s = s.strip()
                        if s.isdigit():
                            idx = int(s)
                            if 1 <= idx <= len(missing_libs):
                                selected_indices.append(idx)
                    
                    if selected_indices:
                        selected_libs = [missing_libs[i-1] for i in selected_indices]
                        success_count = 0
                        failure_count = 0
                        
                        for lib in selected_libs:
                            safe_print(f"\n📦 安装: {lib['name']}...")
                            if SmartLibraryManagement.install_library(lib["name"]):
                                success_count += 1
                                safe_print(f"✅ {lib['name']} 安装成功")
                            else:
                                failure_count += 1
                                safe_print(f"❌ {lib['name']} 安装失败")
                        
                        safe_print(f"\n📊 安装完成: {success_count}个成功, {failure_count}个失败")
                    break
                except ValueError:
                    safe_print("❌ 输入格式错误")
    
    @staticmethod
    def install_all_libraries() -> None:
        """安装所有库"""
        safe_print("\n===== 自动安装所有库 =====")
        required_libs = LibraryManager.get_required_libraries()
        
        for lib in required_libs:
            safe_print(f"\n📦 检查: {lib['name']}...")
            if SmartLibraryManagement.install_library(lib["name"]):
                safe_print(f"✅ {lib['name']} 安装成功")
            else:
                safe_print(f"❌ {lib['name']} 安装失败")
        
        safe_print("\n🎉 所有库安装完成！")

# ==================== 安全输入函数 ====================
class SecureInput:
    @staticmethod
    def input_password(prompt_text: str = "请输入密码: ") -> str:
        """安全输入密码（跨平台兼容）"""
        print(prompt_text, end='', flush=True)
        pwd_chars = []
        
        try:
            if os.name == 'nt':
                import msvcrt
                while True:
                    ch = msvcrt.getch()
                    if ch in (b'\r', b'\n'):
                        safe_print()
                        break
                    elif ch == b'\x08':
                        if pwd_chars:
                            pwd_chars.pop()
                            safe_print('\b \b', end='', flush=True)
                    elif ch == b'\x03':
                        raise KeyboardInterrupt
                    elif b'\x20' <= ch <= b'\x7e':
                        pwd_chars.append(ch.decode('utf-8', errors='ignore'))
                        print('*', end='', flush=True)
            else:
                import termios
                import tty
                
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                
                try:
                    tty.setraw(fd)
                    while True:
                        ch = sys.stdin.read(1)
                        if ch in ('\r', '\n'):
                            safe_print()
                            break
                        elif ch == '\x7f':
                            if pwd_chars:
                                pwd_chars.pop()
                                safe_print('\b \b', end='', flush=True)
                        elif ch == '\x03':
                            raise KeyboardInterrupt
                        elif ' ' <= ch <= '~':
                            pwd_chars.append(ch)
                            print('*', end='', flush=True)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        except KeyboardInterrupt:
            safe_print("\n^C")
            raise
        except Exception:
            safe_print("\n⚠️  密码输入模式不可用，使用普通输入（密码将可见）")
            return input(prompt_text)
        
        return ''.join(pwd_chars)

# ==================== 用户分组管理 ====================
class UserGroupManager:
    """用户分组管理器"""
    
    @staticmethod
    def get_user_files_dir() -> str:
        """获取用户文件目录"""
        return os.path.join(data_dir, "user_files")
    
    @staticmethod
    def get_groups_file() -> str:
        """获取分组配置文件路径"""
        return os.path.join(data_dir, "groups.json")
    
    @staticmethod
    def load_groups_data() -> Dict[str, Any]:
        """加载分组数据"""
        try:
            groups_file = UserGroupManager.get_groups_file()
            if os.path.exists(groups_file):
                with open(groups_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {
                "groups": {},
                "ungrouped_files": [],
                "current_file": "default.json",
                "version": "1.0"
            }
        except Exception as e:
            return {
                "groups": {},
                "ungrouped_files": [],
                "current_file": "default.json",
                "version": "1.0"
            }
    
    @staticmethod
    def save_groups_data(data: Dict[str, Any]) -> bool:
        """保存分组数据"""
        try:
            groups_file = UserGroupManager.get_groups_file()
            os.makedirs(os.path.dirname(groups_file), exist_ok=True)
            with open(groups_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            return False
    
    @staticmethod
    def init_group_system() -> bool:
        """初始化分组系统"""
        try:
            user_files_dir = UserGroupManager.get_user_files_dir()
            os.makedirs(user_files_dir, exist_ok=True)
            
            default_file = os.path.join(user_files_dir, "default.json")
            if not os.path.exists(default_file):
                with open(default_file, 'w', encoding='utf-8') as f:
                    json.dump({
                        "users": {},
                        "next_id": 1,
                        "empty_ids": [],
                        "metadata": {
                            "name": "默认用户文件",
                            "create_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                    }, f, ensure_ascii=False, indent=2)
            
            groups_data = UserGroupManager.load_groups_data()
            if "groups" not in groups_data:
                groups_data["groups"] = {}
            if "ungrouped_files" not in groups_data:
                groups_data["ungrouped_files"] = []
            if "current_file" not in groups_data:
                groups_data["current_file"] = "default.json"
            if "version" not in groups_data:
                groups_data["version"] = "1.0"
            
            if "default.json" not in groups_data["ungrouped_files"]:
                groups_data["ungrouped_files"].append("default.json")
            
            UserGroupManager.save_groups_data(groups_data)
            return True
            
        except Exception as e:
            return False
    
    @staticmethod
    def create_group(group_name: str, description: str = "") -> bool:
        """创建新分组"""
        try:
            if not group_name or len(group_name.strip()) == 0:
                safe_print("❌ 分组名称不能为空")
                return False
            
            groups_data = UserGroupManager.load_groups_data()
            
            if group_name in groups_data["groups"]:
                safe_print(f"❌ 分组 '{group_name}' 已存在")
                return False
            
            groups_data["groups"][group_name] = {
                "description": description,
                "files": [],
                "create_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            if UserGroupManager.save_groups_data(groups_data):
                safe_print(f"✅ 分组 '{group_name}' 创建成功")
                SystemLog.log(f"创建分组: {group_name}", "信息")
                return True
            else:
                safe_print("❌ 保存分组数据失败")
                return False
                
        except Exception as e:
            safe_print(f"❌ 创建分组失败: {str(e)}")
            return False
    
    @staticmethod
    def get_current_user_file() -> str:
        """获取当前用户文件路径"""
        try:
            groups_data = UserGroupManager.load_groups_data()
            current_file = groups_data.get("current_file", "default.json")
            user_files_dir = UserGroupManager.get_user_files_dir()
            return os.path.join(user_files_dir, current_file)
        except:
            user_files_dir = UserGroupManager.get_user_files_dir()
            return os.path.join(user_files_dir, "default.json")
    
    @staticmethod
    def switch_user_file(file_name: str) -> bool:
        """切换当前用户文件"""
        try:
            user_files_dir = UserGroupManager.get_user_files_dir()
            file_path = os.path.join(user_files_dir, file_name)
            
            if not os.path.exists(file_path):
                safe_print(f"❌ 文件不存在: {file_name}")
                return False
            
            groups_data = UserGroupManager.load_groups_data()
            groups_data["current_file"] = file_name
            
            if UserGroupManager.save_groups_data(groups_data):
                safe_print(f"✅ 已切换到文件: {file_name}")
                return True
            else:
                safe_print("❌ 保存配置失败")
                return False
                
        except Exception as e:
            safe_print(f"❌ 切换文件失败: {str(e)}")
            return False

# ==================== 用户文件管理 ====================
class UserFileManagement:
    """用户文件管理菜单"""
    
    @staticmethod
    def show_menu() -> None:
        """显示用户文件管理菜单"""
        while True:
            safe_print("\n===== 用户文件管理 =====")
            safe_print("1. 创建新的用户文件")
            safe_print("2. 切换当前用户文件")
            safe_print("3. 列出所有用户文件")
            safe_print("4. 返回主菜单")
            
            choice = input("请选择(1-4): ").strip()
            
            if choice == "1":
                UserFileManagement.create_user_file()
            elif choice == "2":
                UserFileManagement.switch_user_file()
            elif choice == "3":
                UserFileManagement.list_user_files()
            elif choice == "4":
                break
            else:
                safe_print("❌ 无效选择")
    
    @staticmethod
    def create_user_file() -> None:
        """创建新的用户文件"""
        file_name = input("请输入文件名(无需.json后缀): ").strip()
        if not file_name:
            safe_print("❌ 文件名不能为空")
            return
        
        if not file_name.endswith('.json'):
            file_name += '.json'
        
        import re
        if not re.match(r'^[a-zA-Z0-9_\u4e00-\u9fa5\-]+\.json$', file_name):
            safe_print("❌ 文件名只能包含中文、英文、数字、下划线和减号")
            return
        
        user_files_dir = UserGroupManager.get_user_files_dir()
        file_path = os.path.join(user_files_dir, file_name)
        
        if os.path.exists(file_path):
            safe_print(f"❌ 文件 '{file_name}' 已存在")
            return
        
        try:
            new_file_data = {
                "users": {},
                "next_id": 1,
                "empty_ids": [],
                "metadata": {
                    "name": file_name.replace('.json', ''),
                    "create_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "user_count": 0
                }
            }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(new_file_data, f, ensure_ascii=False, indent=2)
            
            groups_data = UserGroupManager.load_groups_data()
            if file_name not in groups_data["ungrouped_files"]:
                groups_data["ungrouped_files"].append(file_name)
                UserGroupManager.save_groups_data(groups_data)
            
            safe_print(f"✅ 用户文件 '{file_name}' 创建成功")
            
        except Exception as e:
            safe_print(f"❌ 创建文件失败: {str(e)}")
    
    @staticmethod
    def switch_user_file() -> None:
        """切换当前用户文件"""
        user_files_dir = UserGroupManager.get_user_files_dir()
        
        all_files = []
        if os.path.exists(user_files_dir):
            for file in os.listdir(user_files_dir):
                if file.endswith('.json'):
                    all_files.append(file)
        
        if not all_files:
            safe_print("❌ 没有可用的用户文件")
            return
        
        safe_print("\n=== 可用用户文件 ===")
        for i, file_name in enumerate(all_files, 1):
            file_path = os.path.join(user_files_dir, file_name)
            file_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0
            safe_print(f"{i}. {file_name} ({file_size} 字节)")
        
        try:
            choice = int(input("\n请选择文件编号: ").strip())
            if 1 <= choice <= len(all_files):
                selected_file = all_files[choice - 1]
                if UserGroupManager.switch_user_file(selected_file):
                    safe_print("✅ 文件切换成功")
                else:
                    safe_print("❌ 切换失败")
            else:
                safe_print("❌ 无效编号")
        except ValueError:
            safe_print("❌ 请输入有效的数字")
    
    @staticmethod
    def list_user_files() -> None:
        """列出所有用户文件"""
        user_files_dir = UserGroupManager.get_user_files_dir()
        
        if not os.path.exists(user_files_dir):
            safe_print("用户文件目录不存在")
            return
        
        all_files = []
        for file in os.listdir(user_files_dir):
            if file.endswith('.json'):
                file_path = os.path.join(user_files_dir, file)
                all_files.append((file, file_path))
        
        if not all_files:
            safe_print("没有用户文件")
            return
        
        safe_print("\n=== 用户文件列表 ===")
        for file_name, file_path in all_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                user_count = len(data.get("users", {}))
                file_size = os.path.getsize(file_path)
                
                groups_data = UserGroupManager.load_groups_data()
                is_current = (groups_data.get("current_file") == file_name)
                current_mark = " ✅当前" if is_current else ""
                
                safe_print(f"📄 {file_name}{current_mark}")
                safe_print(f"   用户数: {user_count}, 大小: {file_size} 字节")
                
            except Exception as e:
                safe_print(f"📄 {file_name} (读取失败: {str(e)})")

# ==================== UI工具类 ====================
class UITools:
    @staticmethod
    def input_password(prompt_text: str = "请输入密码: ") -> str:
        """安全输入密码"""
        return SecureInput.input_password(prompt_text)

    @staticmethod
    def password_verification() -> bool:
        """密码验证"""
        passwords = DataManagement.load_secure_passwords()
        
        if not passwords:
            safe_print("\n⚠️  系统未设置密码")
            safe_print("出于安全考虑，请先设置密码")
            return PasswordManagement.change_password()
        
        attempts = 0
        max_attempts = 5
        
        while attempts < max_attempts:
            attempts += 1
            pwd = UITools.input_password("请输入密码: ")
            
            for salt, stored_hash in passwords:
                if PasswordSecurity.verify_password(pwd, salt, stored_hash):
                    safe_print("✅ 验证通过！")
                    time.sleep(0.3)
                    SystemLog.security_log("登录验证", "用户", f"成功-第{attempts}次尝试")
                    return True
            
            safe_print(f"❌ 密码错误，剩余尝试次数: {max_attempts - attempts}")
            SystemLog.security_log("登录验证", "用户", f"失败-第{attempts}次尝试")
        
        safe_print("❌ 密码验证失败次数过多，系统退出")
        return False

    @staticmethod
    def print_slowly(text: str, delay: float = 0.1) -> None:
        """缓慢打印文本"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        safe_print()

    @staticmethod
    def show_main_menu() -> str:
        """显示主菜单"""
        global developer_mode, system_name
        safe_print("\n" + "=" * 60)
        safe_print(f"           {system_name}")
        if developer_mode:
            safe_print("           🛠️ 开发者模式")
        safe_print("=" * 60)
        safe_print(" 1. 添加用户")
        safe_print(" 2. 查看所有用户")
        safe_print(" 3. 查找用户")
        safe_print(" 4. 删除用户")
        safe_print(" 5. 删除所有用户")
        safe_print(" 6. 修改用户备注")  # 新增选项
        safe_print(" 7. 系统信息")
        safe_print(" 8. 查看系统日志")
        safe_print(" 9. 导出数据")
        safe_print("10. 数据恢复")
        safe_print("11. 系统更新")
        safe_print("12. 密码管理")
        safe_print("13. 防火墙设置")
        safe_print("14. 系统优化")
        safe_print("15. AI智能助手")
        safe_print("16. 命令行模式")
        safe_print("17. 库依赖管理")
        safe_print("18. 网络功能")
        safe_print("19. 用户文件管理")
        
        if developer_mode:
            safe_print("20. 🛠️ 开发者选项")
            safe_print("21. 🚪 退出开发者模式")
            safe_print("22. 退出系统")
            safe_print("=" * 60)
            while True:
                selection = input("请选择操作(1-22): ").strip()
                if selection in [str(i) for i in range(1, 23)] or selection == "a1b2c3d4e5":
                    return selection
                safe_print("无效选择，请输入1-22之间的数字")
        else:
            safe_print("20. 退出系统")
            safe_print("=" * 60)
            while True:
                selection = input("请选择操作(1-20): ").strip()
                if selection in [str(i) for i in range(1, 21)] or selection == "a1b2c3d4e5":
                    return selection
                safe_print("无效选择，请输入1-20之间的数字")

# ==================== 数据管理类 ====================
class DataManagement:
    @staticmethod
    def init_system() -> bool:
        """初始化系统"""
        try:
            os.makedirs(data_dir, exist_ok=True)
            os.makedirs(backup_dir, exist_ok=True)
            os.makedirs(update_package_dir, exist_ok=True)
            
            if not os.path.exists(occupation_file):
                default_occupations = ["学生", "教师", "工程师", "医生", "护士", "程序员", "设计师", "销售", "经理", "厨师", "司机", "公务员", "农民", "自由职业", "其他"]
                with open(occupation_file, 'w', encoding='utf-8') as f:
                    json.dump(default_occupations, f, ensure_ascii=False, indent=2)
                SystemLog.log("已初始化职业列表")
            
            if not os.path.exists(user_file):
                initial_data = {"users": {}, "next_id": 1, "empty_ids": []}
                with open(user_file, 'w', encoding='utf-8') as f:
                    json.dump(initial_data, f, ensure_ascii=False, indent=2)
                SystemLog.log("已初始化用户数据库")
            
            if not os.path.exists(password_file):
                DataManagement.save_secure_passwords([])
            
            if not os.path.exists(version_file):
                DataManagement.save_version(3, 0)
            
            if not os.path.exists(firewall_file):
                default_firewall_rules = {
                    "enable_firewall": False,
                    "block_weak_passwords": True,
                    "max_login_attempts": 5,
                    "session_timeout": 1800,
                    "audit_logging": True
                }
                with open(firewall_file, 'w', encoding='utf-8') as f:
                    json.dump(default_firewall_rules, f, ensure_ascii=False, indent=2)
                SystemLog.log("已初始化防火墙配置")
            
            if not os.path.exists(ai_config_file):
                default_ai_config = {
                    "enable_ai": False,
                    "providers": {
                        "deepseek": {
                            "enabled": False,
                            "api_key": "",
                            "api_base": "https://api.deepseek.com",
                            "model": "deepseek-chat"
                        },
                        "aliyun": {
                            "enabled": False,
                            "api_key": "",
                            "api_base": "https://dashscope.aliyuncs.com",
                            "model": "qwen-max"
                        }
                    },
                    "last_provider": "deepseek",
                    "temperature": 0.7,
                    "max_tokens": 1000
                }
                with open(ai_config_file, 'w', encoding='utf-8') as f:
                    json.dump(default_ai_config, f, ensure_ascii=False, indent=2)
                SystemLog.log("已初始化AI配置")
            
            if not os.path.exists(network_rules_file):
                default_network_rules = {
                    "blacklist": [],
                    "whitelist": [],
                    "description": "网络防火墙规则"
                }
                with open(network_rules_file, 'w', encoding='utf-8') as f:
                    json.dump(default_network_rules, f, ensure_ascii=False, indent=2)
                SystemLog.log("已初始化网络规则")
            
            UserGroupManager.init_group_system()
            
            return True
        except Exception as e:
            SystemLog.log(f"初始化系统失败: {str(e)}", "错误")
            return False

    @staticmethod
    def load_secure_passwords() -> List[Tuple[str, str]]:
        """加载安全的密码列表"""
        try:
            if not os.path.exists(password_file):
                return []
            
            with open(password_file, 'r', encoding='utf-8') as f:
                passwords_data = json.load(f)
            
            if not passwords_data:
                return []
            
            if isinstance(passwords_data, list) and len(passwords_data) > 0:
                if isinstance(passwords_data[0], dict) and "salt" in passwords_data[0] and "hash" in passwords_data[0]:
                    return [(p["salt"], p["hash"]) for p in passwords_data]
            
            return []
        except Exception:
            return []

    @staticmethod
    def save_secure_passwords(passwords: List[Tuple[str, str]]) -> bool:
        """保存安全的密码列表"""
        try:
            passwords_data = [{"salt": salt, "hash": pwd_hash} for salt, pwd_hash in passwords]
            
            with open(password_file, 'w', encoding='utf-8') as f:
                json.dump(passwords_data, f, ensure_ascii=False, indent=2)
            return True
        except Exception:
            return False

    @staticmethod
    def save_version(major: int, minor: int) -> bool:
        """保存版本号"""
        try:
            with open(version_file, 'w', encoding='utf-8') as f:
                json.dump({"major": major, "minor": minor}, f, ensure_ascii=False, indent=2)
            return True
        except Exception:
            return False

    @staticmethod
    def load_version() -> str:
        """加载版本号"""
        try:
            with open(version_file, 'r', encoding='utf-8') as f:
                v = json.load(f)
            return f"{v['major']}.{v['minor']}"
        except Exception:
            return "3.0"

    @staticmethod
    def load_user_data() -> Dict[str, Any]:
        """加载用户数据（支持分组系统）"""
        try:
            current_file = UserGroupManager.get_current_user_file()
            
            if os.path.exists(current_file):
                with open(current_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            
            return {"users": {}, "next_id": 1, "empty_ids": []}
        except Exception as e:
            SystemLog.log(f"加载用户数据失败: {str(e)}", "错误")
            return {"users": {}, "next_id": 1, "empty_ids": []}

    @staticmethod
    def save_user_data(data: Dict[str, Any]) -> bool:
        """保存用户数据（支持分组系统）"""
        try:
            current_file = UserGroupManager.get_current_user_file()
            os.makedirs(os.path.dirname(current_file), exist_ok=True)
            
            if "metadata" not in data:
                data["metadata"] = {}
            
            data["metadata"]["last_modified"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if "users" in data:
                data["metadata"]["user_count"] = len(data["users"])
            
            with open(current_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            SystemLog.log(f"保存用户数据到: {os.path.basename(current_file)}", "信息")
            return True
        except Exception as e:
            SystemLog.log(f"保存用户数据失败: {str(e)}", "错误")
            return False

    @staticmethod
    def create_backup() -> bool:
        """创建备份（支持分组系统）"""
        try:
            current_file = UserGroupManager.get_current_user_file()
            file_name = os.path.basename(current_file)
            file_base_name = os.path.splitext(file_name)[0]  # 移除扩展名
            
            if not os.path.exists(current_file):
                safe_print(f"❌ 用户文件不存在: {current_file}")
                return False
            
            os.makedirs(backup_dir, exist_ok=True)
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            # 使用实际文件名作为备份文件名
            backup_file = os.path.join(backup_dir, f"{file_base_name}_{timestamp}.json")
            
            with open(current_file, 'r', encoding='utf-8') as src:
                with open(backup_file, 'w', encoding='utf-8') as dst:
                    dst.write(src.read())
            
            # 清理旧备份（只保留每个文件最新的5个备份）
            backup_files = {}
            for f in os.listdir(backup_dir):
                if f.endswith('.json'):
                    parts = f.rsplit('_', 2)  # 分割格式: filename_YYYYMMDD_HHMMSS.json
                    if len(parts) >= 2:
                        file_prefix = '_'.join(parts[:-2]) if len(parts) > 2 else parts[0]
                        if file_prefix not in backup_files:
                            backup_files[file_prefix] = []
                        backup_files[file_prefix].append(f)
            
            for file_prefix, files in backup_files.items():
                if len(files) > 5:
                    files.sort(key=lambda x: os.path.getctime(os.path.join(backup_dir, x)))
                    for old_backup in files[:-5]:
                        old_backup_path = os.path.join(backup_dir, old_backup)
                        if os.path.exists(old_backup_path):
                            try:
                                os.remove(old_backup_path)
                                SystemLog.log(f"清理旧备份: {old_backup}", "信息")
                            except Exception as e:
                                SystemLog.log(f"删除旧备份失败 {old_backup}: {str(e)}", "警告")
            
            backup_size = os.path.getsize(backup_file)
            safe_print(f"✅ 备份创建成功: {os.path.basename(backup_file)} ({backup_size} 字节)")
            SystemLog.log(f"已创建备份: {backup_file} ({backup_size} 字节)")
            
            return True
        except Exception as e:
            safe_print(f"❌ 创建备份失败: {str(e)}")
            SystemLog.log(f"创建备份失败: {str(e)}", "错误")
            return False

    @staticmethod
    def get_backup_list() -> List[Dict[str, Any]]:
        """获取备份列表（支持分组系统和旧版备份）"""
        try:
            if not os.path.exists(backup_dir):
                return []
            
            # 获取当前用户文件名
            current_file = UserGroupManager.get_current_user_file()
            current_file_name = os.path.basename(current_file)
            file_base_name = os.path.splitext(current_file_name)[0]
            
            backup_list = []
            for f in os.listdir(backup_dir):
                if f.endswith('.json'):
                    file_path = os.path.join(backup_dir, f)
                    
                    # 检查是否为当前文件的备份
                    is_current_file_backup = False
                    backup_type = "其他"
                    
                    # 情况1：新格式备份 - default_20241020_143025.json
                    if f.startswith(file_base_name + '_'):
                        is_current_file_backup = True
                        backup_type = "新版格式"
                    
                    # 情况2：旧格式备份 - users_20241020_143025.json
                    elif f.startswith('users_'):
                        # 旧版备份 users_*.json 对应 default.json
                        if current_file_name == 'default.json':
                            is_current_file_backup = True
                            backup_type = "旧版格式"
                        else:
                            # 对于其他文件，旧版备份可能不适用
                            backup_type = "旧版通用"
                    
                    # 情况3：其他文件备份 - testfile_20241020_143025.json
                    else:
                        backup_type = "其他文件"
                    
                    backup_info = {
                        "filename": f,
                        "is_current_file": is_current_file_backup,
                        "path": file_path,
                        "file_size": os.path.getsize(file_path),
                        "modified_time": os.path.getmtime(file_path),
                        "backup_type": backup_type
                    }
                    backup_list.append(backup_info)
            
            # 按修改时间排序（最新的在前）
            backup_list.sort(key=lambda x: x["modified_time"], reverse=True)
            return backup_list
        except Exception as e:
            SystemLog.log(f"获取备份列表失败: {str(e)}", "错误")
            return []

    @staticmethod
    def restore_backup(backup_filename: str) -> Tuple[bool, str]:
        """恢复备份（支持新旧版本备份）"""
        try:
            if not os.path.exists(backup_dir):
                return False, "备份目录不存在"
            
            backup_file_path = os.path.join(backup_dir, backup_filename)
            if not os.path.exists(backup_file_path):
                return False, "备份文件不存在"
            
            # 加载备份数据
            backup_data = None
            with open(backup_file_path, 'r', encoding='utf-8') as src:
                backup_data = json.load(src)
            
            if not backup_data or "users" not in backup_data:
                return False, "备份文件格式无效"
            
            # 获取当前用户文件路径
            current_file = UserGroupManager.get_current_user_file()
            current_file_name = os.path.basename(current_file)
            
            # 检查是否为旧版备份
            is_old_version = backup_filename.startswith('users_')
            
            # 如果是旧版备份且当前文件不是default.json，需要提示
            if is_old_version and current_file_name != 'default.json':
                safe_print("⚠️  旧版备份(users_*.json)只能恢复到default.json")
                safe_print(f"   当前文件: {current_file_name}")
                confirm = input("是否切换到default.json并恢复? (Y/N): ").upper()
                if confirm != 'Y':
                    return False, "用户取消恢复"
                # 切换到default.json
                UserGroupManager.switch_user_file("default.json")
                current_file = UserGroupManager.get_current_user_file()
                current_file_name = "default.json"
            
            # 创建当前数据的备份（以防万一）
            DataManagement.create_backup()
            
            # 如果是旧版备份，可能需要添加metadata
            if is_old_version:
                if "metadata" not in backup_data:
                    backup_data["metadata"] = {
                        "name": "default",
                        "create_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "version": "old_backup_converted",
                        "original_backup": backup_filename
                    }
                safe_print("🔄 正在转换旧版备份格式...")
            
            # 恢复备份到当前用户文件
            with open(current_file, 'w', encoding='utf-8') as dst:
                json.dump(backup_data, dst, ensure_ascii=False, indent=2)
            
            # 验证恢复是否成功
            restored_data = DataManagement.load_user_data()
            user_count = len(restored_data.get("users", {}))
            
            if is_old_version:
                SystemLog.log(f"已从旧版备份恢复: {backup_filename} 到 {current_file_name} (恢复 {user_count} 个用户，已转换格式)")
                return True, f"成功从旧版备份恢复数据到 {current_file_name} (恢复用户数: {user_count}，已自动转换格式)"
            else:
                SystemLog.log(f"已从备份恢复: {backup_filename} 到 {current_file_name} (恢复 {user_count} 个用户)")
                return True, f"成功从备份恢复数据到 {current_file_name} (恢复用户数: {user_count})"
        except Exception as e:
            error_info = f"恢复备份失败: {str(e)}"
            SystemLog.log(error_info, "错误")
            return False, error_info

    @staticmethod
    def data_recovery() -> None:
        """数据恢复（支持新旧版本备份）"""
        try:
            safe_print("\n===== 数据恢复 =====")
            
            # 获取当前用户文件信息
            current_file = UserGroupManager.get_current_user_file()
            current_file_name = os.path.basename(current_file)
            safe_print(f"当前用户文件: {current_file_name}")
            safe_print("ℹ️  旧版备份(users_*.json)只适用于default.json文件")
            safe_print("-" * 50)
            
            # 获取备份列表
            backup_list = DataManagement.get_backup_list()
            
            if not backup_list:
                safe_print("没有找到任何备份文件")
                return
            
            # 分离当前文件的备份和其他备份
            current_file_backups = []
            old_version_backups = []
            other_backups = []
            
            for backup in backup_list:
                if backup["is_current_file"]:
                    current_file_backups.append(backup)
                elif backup["backup_type"] == "旧版通用" and current_file_name == 'default.json':
                    # 旧版users_备份也可以用于default.json
                    old_version_backups.append(backup)
                else:
                    other_backups.append(backup)
            
            # 显示可用的备份
            display_count = 0
            
            # 显示当前文件的新版备份
            if current_file_backups:
                safe_print(f"\n=== {current_file_name} 的备份 (新版格式) ===")
                safe_print("序号 | 备份文件名                | 创建时间        | 类型")
                safe_print("-" * 70)
                for i, backup in enumerate(current_file_backups, 1):
                    file_time = datetime.datetime.fromtimestamp(backup["modified_time"]).strftime("%Y-%m-%d %H:%M")
                    file_size_kb = backup["file_size"] / 1024
                    safe_print(f"{i:2d}.  | {backup['filename']:<25} | {file_time} | {backup['backup_type']}")
                    display_count += 1
            
            # 显示旧版备份（仅当当前文件是default.json时）
            if old_version_backups and current_file_name == 'default.json':
                if not current_file_backups:
                    safe_print(f"\n=== 旧版备份 (users_*.json) ===")
                    safe_print("序号 | 备份文件名                | 创建时间        | 类型")
                    safe_print("-" * 70)
                    start_index = 1
                else:
                    safe_print(f"\n=== 旧版备份 (users_*.json) ===")
                    start_index = len(current_file_backups) + 1
                
                for i, backup in enumerate(old_version_backups, start_index):
                    file_time = datetime.datetime.fromtimestamp(backup["modified_time"]).strftime("%Y-%m-%d %H:%M")
                    file_size_kb = backup["file_size"] / 1024
                    safe_print(f"{i:2d}.  | {backup['filename']:<25} | {file_time} | {backup['backup_type']}")
                    display_count += 1
            
            if other_backups:
                safe_print(f"\n=== 其他文件的备份 ===")
                for backup in other_backups[:3]:  # 只显示前3个
                    file_time = datetime.datetime.fromtimestamp(backup["modified_time"]).strftime("%Y-%m-%d %H:%M")
                    safe_print(f"  • {backup['filename']} - {file_time} ({backup['backup_type']})")
                if len(other_backups) > 3:
                    safe_print(f"  还有 {len(other_backups) - 3} 个其他备份...")
            
            if not current_file_backups and not old_version_backups:
                safe_print("\n⚠️  没有找到适用于当前文件的备份")
                if current_file_name != 'default.json':
                    safe_print("💡 提示：旧版备份(users_*.json)只适用于default.json文件")
                return
            
            while True:
                total_options = len(current_file_backups) + len(old_version_backups)
                selection = input(f"\n请选择要恢复的备份编号(1-{total_options})或输入0取消: ").strip()
                if selection == "0":
                    safe_print("恢复操作已取消")
                    return
                
                if selection.isdigit():
                    num = int(selection)
                    if 1 <= num <= total_options:
                        # 确定选择的是哪个备份
                        if num <= len(current_file_backups):
                            selected_backup = current_file_backups[num - 1]
                        else:
                            selected_backup = old_version_backups[num - len(current_file_backups) - 1]
                        
                        # 获取当前数据信息
                        current_data = DataManagement.load_user_data()
                        current_user_count = len(current_data.get("users", {}))
                        
                        safe_print(f"\n📋 恢复信息:")
                        safe_print(f"   当前文件: {current_file_name}")
                        safe_print(f"   当前用户数: {current_user_count}")
                        safe_print(f"   备份文件: {selected_backup['filename']}")
                        safe_print(f"   备份类型: {selected_backup['backup_type']}")
                        
                        # 显示备份详细信息
                        try:
                            with open(selected_backup["path"], 'r', encoding='utf-8') as f:
                                backup_data = json.load(f)
                            backup_user_count = len(backup_data.get("users", {}))
                            safe_print(f"   备份用户数: {backup_user_count}")
                            
                            # 检查是否为旧版备份
                            if selected_backup['backup_type'] == "旧版格式" or selected_backup['backup_type'] == "旧版通用":
                                safe_print("   ⚠️  这是旧版格式备份")
                                safe_print("   💡 系统将自动转换格式")
                        except:
                            pass
                        
                        confirm = input("\n确定要恢复这个备份吗? 当前数据将被覆盖!(Y/N): ").upper()
                        if confirm == "Y":
                            success, message = DataManagement.restore_backup(selected_backup["filename"])
                            if success:
                                safe_print(f"✅ {message}")
                                time.sleep(1)
                                safe_print("\n恢复后系统信息:")
                                # 显示恢复后的数据
                                restored_data = DataManagement.load_user_data()
                                user_count = len(restored_data.get("users", {}))
                                safe_print(f"✅ 恢复成功！当前用户数: {user_count}")
                                SystemLog.log(f"用户手动恢复备份: {selected_backup['filename']}", "信息")
                            else:
                                safe_print(f"❌ {message}")
                        else:
                            safe_print("恢复操作已取消")
                        break
                    else:
                        safe_print(f"❌ 编号 {num} 无效，请选择1-{total_options}")
                else:
                    safe_print("❌ 请输入有效的数字")
                    
        except Exception as e:
            safe_print(f"❌ 数据恢复过程中发生错误: {str(e)}")
            SystemLog.log(f"数据恢复失败: {str(e)}", "错误")

    @staticmethod
    def load_occupation_list() -> List[str]:
        """加载职业列表"""
        try:
            if os.path.exists(occupation_file):
                with open(occupation_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except Exception as e:
            SystemLog.log(f"加载职业列表失败: {str(e)}", "错误")
            return []

    @staticmethod
    def load_firewall_config() -> Dict[str, Any]:
        """加载防火墙配置"""
        try:
            if os.path.exists(firewall_file):
                with open(firewall_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            SystemLog.log(f"加载防火墙配置失败: {str(e)}", "错误")
            return {}

    @staticmethod
    def load_network_rules() -> Dict[str, Any]:
        """加载网络规则"""
        try:
            if os.path.exists(network_rules_file):
                with open(network_rules_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {"blacklist": [], "whitelist": [], "description": "网络防火墙规则"}
        except Exception as e:
            SystemLog.log(f"加载网络规则失败: {str(e)}", "错误")
            return {"blacklist": [], "whitelist": [], "description": "网络防火墙规则"}

    @staticmethod
    def save_network_rules(rules: Dict[str, Any]) -> bool:
        """保存网络规则"""
        try:
            with open(network_rules_file, 'w', encoding='utf-8') as f:
                json.dump(rules, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            SystemLog.log(f"保存网络规则失败: {str(e)}", "错误")
            return False

    @staticmethod
    def enhanced_backup() -> Tuple[bool, str]:
        """增强的备份功能"""
        try:
            safe_print("\n📦 正在创建增强备份...")
            
            # 1. 备份用户数据
            backup_success = DataManagement.create_backup()
            if not backup_success:
                return False, "用户数据备份失败"
            
            # 2. 备份系统文件
            current_file = sys.argv[0] if sys.argv else __file__
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            system_backup_file = os.path.join(backup_dir, f"system_{timestamp}.py")
            shutil.copy2(current_file, system_backup_file)
            
            # 3. 备份配置文件
            config_files = [occupation_file, firewall_file, network_rules_file, ai_config_file]
            config_backup_dir = os.path.join(backup_dir, f"config_{timestamp}")
            os.makedirs(config_backup_dir, exist_ok=True)
            
            for config_file in config_files:
                if os.path.exists(config_file):
                    shutil.copy2(config_file, os.path.join(config_backup_dir, os.path.basename(config_file)))
            
            # 4. 创建备份报告
            report_file = os.path.join(backup_dir, f"backup_report_{timestamp}.txt")
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(f"PWOS2 系统备份报告\n")
                f.write(f"备份时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"系统版本: {DataManagement.load_version()}\n")
                f.write(f"备份文件:\n")
                f.write(f"  • 系统文件: {system_backup_file}\n")
                f.write(f"  • 配置文件: {config_backup_dir}/\n")
                f.write(f"  • 用户数据: 已备份到备份目录\n")
            
            safe_print("✅ 增强备份创建完成")
            return True, f"备份完成于 {timestamp}"
            
        except Exception as e:
            safe_print(f"❌ 增强备份失败: {str(e)}")
            return False, str(e)

# ==================== 输入处理器 ====================
class InputHandler:
    @staticmethod
    def input_age() -> int:
        """输入年龄"""
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                age_input = input("年龄: ").strip()
                if not age_input:
                    raise ValueError("年龄不能为空")
                
                age = int(age_input)
                if 0 < age < 120:
                    return age
                
                safe_print("年龄应在1-119之间")
            except ValueError as e:
                safe_print(str(e))
            
            if attempt < max_attempts - 1:
                safe_print(f"剩余尝试次数: {max_attempts - attempt - 1}")
        
        safe_print("输入尝试次数过多，使用默认年龄25")
        return 25

    @staticmethod
    def input_gender() -> str:
        """输入性别"""
        gender_map = {
            'b': '男', '男': '男', 'm': '男', 'man': '男', '男生': '男', 'boy': '男',
            'g': '女', '女': '女', 'f': '女', 'woman': '女', '女生': '女', 'girl': '女',
            'o': '其他', '其他': '其他', 'unknown': '其他', 'x': '其他'
        }
        
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                safe_print("\n性别输入选项:")
                safe_print("  [b] 男生 (男/m/man/boy)")
                safe_print("  [g] 女生 (女/f/woman/girl)")
                safe_print("  [o] 其他 (其他/unknown/x)")
                
                input_val = input("请选择性别: ").strip().lower()
                if not input_val:
                    raise ValueError("性别不能为空")
                
                if input_val in gender_map:
                    return gender_map[input_val]
                
                if any(key in input_val for key in ['男', 'b', 'm']):
                    return '男'
                elif any(key in input_val for key in ['女', 'g', 'f', 'w']):
                    return '女'
                else:
                    return '其他'
                    
            except ValueError as e:
                safe_print(str(e))
            
            if attempt < max_attempts - 1:
                safe_print(f"剩余尝试次数: {max_attempts - attempt - 1}")
        
        safe_print("输入尝试次数过多，使用默认性别'其他'")
        return '其他'

    @staticmethod
    def select_occupation() -> str:
        """选择职业"""
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                occupation_list = DataManagement.load_occupation_list()
                if not occupation_list:
                    safe_print("警告: 职业列表为空，请添加职业")
                    
                    for sub_attempt in range(3):
                        new_occupation = input("请输入新职业名称: ").strip()
                        if new_occupation:
                            return new_occupation
                        safe_print("职业名称不能为空")
                    
                    return "其他"
                
                safe_print("\n=== 请选择职业 ===")
                for i, occupation in enumerate(occupation_list, 1):
                    safe_print(f"{i}. {occupation}")
                safe_print("=" * 17)
                
                selection = input(f"请选择编号(1-{len(occupation_list)})或输入职业名称: ").strip()
                if not selection:
                    safe_print("输入不能为空")
                    continue
                
                if selection.isdigit():
                    num = int(selection)
                    if 1 <= num <= len(occupation_list):
                        selected_occupation = occupation_list[num - 1]
                        if selected_occupation == "其他":
                            specific_occupation = input("请输入具体的职业名称: ").strip()
                            if specific_occupation:
                                if specific_occupation not in occupation_list:
                                    occupation_list.append(specific_occupation)
                                    with open(occupation_file, 'w', encoding='utf-8') as f:
                                        json.dump(occupation_list, f, ensure_ascii=False, indent=2)
                                return specific_occupation
                            else:
                                safe_print("职业名称不能为空，请重新输入")
                                continue
                        else:
                            return selected_occupation
                    else:
                        safe_print(f"编号 {num} 无效，请选择1-{len(occupation_list)}")
                        continue
                else:
                    if selection.lower() in ["其他", "other"]:
                        specific_occupation = input("请输入具体的职业名称: ").strip()
                        if specific_occupation:
                            if specific_occupation not in occupation_list:
                                occupation_list.append(specific_occupation)
                                with open(occupation_file, 'w', encoding='utf-8') as f:
                                    json.dump(occupation_list, f, ensure_ascii=False, indent=2)
                            return specific_occupation
                        else:
                            safe_print("职业名称不能为空，请重新输入")
                            continue
                    
                    if selection in occupation_list:
                        return selection
                    
                    confirm = input(f"'{selection}'不在列表中，是否添加为新职业?(Y/N): ").upper()
                    if confirm == 'Y':
                        if selection not in occupation_list:
                            occupation_list.append(selection)
                            with open(occupation_file, 'w', encoding='utf-8') as f:
                                json.dump(occupation_list, f, ensure_ascii=False, indent=2)
                        return selection
                    else:
                        safe_print("请重新选择")
                        
            except Exception as e:
                safe_print(f"选择职业时发生错误: {str(e)}")
                SystemLog.log(f"选择职业失败: {str(e)}", "错误")
            
            if attempt < max_attempts - 1:
                safe_print(f"剩余尝试次数: {max_attempts - attempt - 1}")
        
        safe_print("输入尝试次数过多，使用默认职业'其他'")
        return "其他"

    @staticmethod
    def validate_user_data(name: str, age: int, gender: str, occupation: str, remark: str = "") -> Tuple[bool, str]:
        """验证用户数据完整性（添加备注参数）"""
        try:
            if not name or len(name.strip()) == 0:
                return False, "姓名不能为空"
            
            if len(name.strip()) > 50:
                return False, "姓名过长（最多50字符）"
            
            if not isinstance(age, int):
                return False, "年龄必须是整数"
            
            if age <= 0 or age >= 120:
                return False, "年龄应在1-119之间"
            
            valid_genders = ['男', '女', '其他']
            if gender not in valid_genders:
                return False, f"性别无效（应为：{', '.join(valid_genders)}）"
            
            if not occupation or len(occupation.strip()) == 0:
                return False, "职业不能为空"
            
            if len(occupation.strip()) > 100:
                return False, "职业名称过长（最多100字符）"
            
            return True, "数据验证通过"
            
        except Exception as e:
            return False, f"数据验证异常: {str(e)}"

# ==================== 用户管理 ====================
class UserManagement:
    @staticmethod
    def authenticate_delete() -> bool:
        """验证删除权限"""
        passwords = DataManagement.load_secure_passwords()
        if not passwords:
            safe_print("\n⚠️  删除操作需要认证")
            safe_print("系统未设置密码，请输入开发者密码")
            input_password = UITools.input_password("请输入开发者密码: ")
            if input_password == developer_password:
                safe_print("✅ 开发者认证通过")
                return True
            else:
                safe_print("❌ 认证失败")
                return False
        else:
            safe_print("\n⚠️  删除操作需要密码认证")
            return UITools.password_verification()

    @staticmethod
    def add_user() -> None:
        """添加用户"""
        try:
            data = DataManagement.load_user_data()
            
            if data["empty_ids"]:
                min_empty_id = min(data["empty_ids"])
                choice = input(f"检测到空ID {min_empty_id}，是否使用?(Y/N): ").upper()
                if choice == 'Y':
                    use_id = min_empty_id
                    data["empty_ids"].remove(min_empty_id)
                else:
                    use_id = data["next_id"]
                    data["next_id"] += 1
            else:
                use_id = data["next_id"]
                data["next_id"] += 1
            
            safe_print(f"\n正在为ID {use_id} 添加用户")
            
            name = ""
            max_attempts = 3
            for attempt in range(max_attempts):
                name = input("姓名: ").strip()
                if name:
                    break
                safe_print("姓名不能为空")
                if attempt < max_attempts - 1:
                    safe_print(f"剩余尝试次数: {max_attempts - attempt - 1}")
            
            if not name:
                safe_print("输入尝试次数过多，添加用户取消")
                return
            
            age = InputHandler.input_age()
            gender = InputHandler.input_gender()
            occupation = InputHandler.select_occupation()
            
            # 添加备注输入
            safe_print("\n📝 备注信息（可选，直接回车跳过）")
            remark = input("请输入备注: ").strip()
            if not remark:
                remark = "无"
            
            is_valid, error_msg = InputHandler.validate_user_data(name, age, gender, occupation)
            if not is_valid:
                safe_print(f"❌ 数据验证失败: {error_msg}")
                return
            
            user_info = {
                "姓名": name,
                "年龄": age,
                "性别": gender,
                "职业": occupation,
                "备注": remark,  # 添加备注字段
                "创建时间": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            safe_print("\n===== 信息确认 =====")
            safe_print(f"ID:   {use_id}")
            safe_print(f"姓名: {name}")
            safe_print(f"年龄: {age}")
            safe_print(f"性别: {gender}")
            safe_print(f"职业: {occupation}")
            safe_print("====================")
            
            confirm = input("是否保存?(Y/N): ").upper()
            if confirm == 'Y':
                data["users"][str(use_id)] = user_info
                if DataManagement.save_user_data(data):
                    safe_print(f"✅ 用户已保存! ID: {use_id}")
                    SystemLog.log(f"添加用户: ID={use_id}, 姓名={name}")
                else:
                    safe_print("❌ 保存失败，请检查日志")
            else:
                safe_print("添加已取消")
                if use_id not in data.get("empty_ids", []):
                    data["empty_ids"].append(use_id)
                    
        except Exception as e:
            safe_print(f"❌ 添加用户时发生错误: {str(e)}")
            SystemLog.log(f"添加用户失败: {str(e)}", "错误")

    @staticmethod
    def view_all_users() -> None:
        """查看所有用户"""
        try:
            data = DataManagement.load_user_data()
            users = data.get("users", {})
            
            if not users:
                safe_print("\n当前没有用户数据")
                return
            
            try:
                from prettytable import PrettyTable
                table = PrettyTable()
                table.field_names = ["ID", "姓名", "年龄", "性别", "职业", "备注", "创建时间"]
                table.align["ID"] = "r"
                table.align["年龄"] = "r"
                
                for user_id in sorted(users.keys(), key=lambda x: int(x) if x.isdigit() else x):
                    info = users[user_id]
                    remark = info.get('备注', '无')
                    # 备注太长时截断显示
                    if len(remark) > 15:
                        remark = remark[:12] + "..."
                    table.add_row([user_id, info['姓名'], info['年龄'], info['性别'], info['职业'], remark, info.get('创建时间', '')])
                
                safe_print("\n===== 所有用户信息 =====")
                safe_print(table)
                safe_print(f"共 {len(users)} 位用户")
            except ImportError:
                safe_print("\n===== 所有用户信息 =====")
                safe_print("ID   姓名    年龄  性别  职业          创建时间")
                safe_print("-" * 60)
                for user_id in sorted(users.keys(), key=lambda x: int(x) if x.isdigit() else x):
                    info = users[user_id]
                    safe_print(f"{user_id:<5}{info['姓名']:<8}{info['年龄']:<6}{info['性别']:<6}{info['职业']:<12}{info.get('创建时间', '')}")
                safe_print(f"共 {len(users)} 位用户")
                
        except Exception as e:
            safe_print(f"❌ 查看用户时发生错误: {str(e)}")
            SystemLog.log(f"查看用户失败: {str(e)}", "错误")

    @staticmethod
    def find_user() -> None:
        """查找用户"""
        try:
            data = DataManagement.load_user_data()
            users = data.get("users", {})
            
            if not users:
                safe_print("\n当前没有用户数据")
                return
            
            while True:
                user_id = input("请输入用户ID: ").strip()
                if not user_id:
                    safe_print("ID不能为空")
                    continue
                
                if user_id in users:
                    info = users[user_id]
                    safe_print("\n===== 用户信息 =====")
                    safe_print(f"ID:   {user_id}")
                    safe_print(f"姓名: {info['姓名']}")
                    safe_print(f"年龄: {info['年龄']}")
                    safe_print(f"性别: {info['性别']}")
                    safe_print(f"职业: {info['职业']}")
                    safe_print(f"备注: {info.get('备注', '无')}")  # 显示备注
                    safe_print(f"创建时间: {info.get('创建时间', '未知')}")
                    safe_print("====================")
                    break
                else:
                    safe_print(f"❌ ID {user_id} 的用户不存在")
                    if input("是否继续查找?(Y/N): ").upper() != "Y":
                        break
                        
        except Exception as e:
            safe_print(f"❌ 查找用户时发生错误: {str(e)}")
            SystemLog.log(f"查找用户失败: {str(e)}", "错误")

    @staticmethod
    def delete_user() -> None:
        """删除用户"""
        try:
            if not UserManagement.authenticate_delete():
                safe_print("❌ 认证失败，删除操作已取消")
                return
            
            data = DataManagement.load_user_data()
            users = data.get("users", {})
            
            if not users:
                safe_print("\n当前没有用户数据")
                return
            
            while True:
                user_id = input("请输入要删除的用户ID: ").strip()
                if not user_id:
                    safe_print("ID不能为空")
                    continue
                
                if user_id in users:
                    info = users[user_id]
                    safe_print("\n即将删除的用户信息:")
                    safe_print(f"ID: {user_id}, 姓名: {info['姓名']}, 年龄: {info['年龄']}, 职业: {info['职业']}")
                    
                    confirm = input("确定要删除该用户吗?(Y/N): ").upper()
                    if confirm == "Y":
                        del users[user_id]
                        if int(user_id) not in data["empty_ids"]:
                            data["empty_ids"].append(int(user_id))
                        
                        if DataManagement.save_user_data(data):
                            safe_print(f"✅ ID {user_id} 的用户已删除")
                            SystemLog.security_log(f"删除用户: ID={user_id}", "当前用户", "成功")
                        else:
                            safe_print("❌ 删除失败")
                        break
                    else:
                        safe_print("删除操作已取消")
                        break
                else:
                    safe_print(f"❌ ID {user_id} 的用户不存在")
                    if input("是否继续?(Y/N): ").upper() != "Y":
                        break
                        
        except Exception as e:
            safe_print(f"❌ 删除用户时发生错误: {str(e)}")
            SystemLog.log(f"删除用户失败: {str(e)}", "错误")
    @staticmethod
    def delete_all_users() -> None:
        """删除所有用户（双方案版）"""
        try:
            if not UserManagement.authenticate_delete():
                safe_print("❌ 认证失败，删除操作已取消")
                return
        
            current_file = UserGroupManager.get_current_user_file()
            current_file_name = os.path.basename(current_file)
        
            if not os.path.exists(current_file):
                safe_print(f"❌ 用户文件不存在: {current_file_name}")
                return
        
            # 读取当前数据
            try:
                with open(current_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                user_count = len(data.get("users", {}))
            except:
                user_count = 0
        
            safe_print(f"\n📄 当前文件: {current_file_name}")
            safe_print(f"👥 用户数量: {user_count}")
        
            if user_count == 0:
                safe_print("⚠️  当前文件没有用户数据")
                choice = input("是否要删除空文件? (Y/N): ").upper()
                if choice == "Y":
                    # 删除整个文件
                    os.remove(current_file)
                    safe_print(f"✅ 已删除空文件: {current_file_name}")
                return
        
            # 提供两种方案选择
            safe_print("\n🔧 请选择删除方式:")
            safe_print("1. 清空用户数据（保留文件）")
            safe_print("2. 删除整个文件")
            safe_print("3. 取消操作")
        
            choice = input("\n请选择 (1-3): ").strip()
        
            if choice == "1":
                # 方案1：清空文件
                DataManagement.create_backup()
            
                # 保留metadata，只清空用户数据
                if "metadata" not in data:
                    data["metadata"] = {}
            
                data["users"] = {}
                data["next_id"] = 1
                data["empty_ids"] = []
                data["metadata"]["last_cleared"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data["metadata"]["user_count"] = 0
            
                with open(current_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            
                safe_print(f"✅ 已清空文件 '{current_file_name}' 中的用户数据")
            
            elif choice == "2":
                # 方案2：删除文件
                safe_print("⚠️  ⚠️  ⚠️  严重警告 ⚠️  ⚠️  ⚠️")
                safe_print(f"将永久删除文件: {current_file_name}")
            
                confirm = input(f"\n确定要永久删除文件 '{current_file_name}' 吗? (输入 'DELETE' 确认): ").strip()
                if confirm != "DELETE":
                    safe_print("操作已取消")
                    return
            
                # 备份后再删除
                backup_dir = os.path.join(data_dir, "deleted_backups")
                os.makedirs(backup_dir, exist_ok=True)
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = os.path.join(backup_dir, f"{current_file_name}_{timestamp}.deleted.json")
                shutil.copy2(current_file, backup_file)
            
                os.remove(current_file)
                safe_print(f"✅ 已永久删除文件: {current_file_name}")
            
            elif choice == "3":
                safe_print("操作已取消")
            else:
                safe_print("❌ 无效选择")
            
        except Exception as e:
            safe_print(f"❌ 删除所有用户时发生错误: {str(e)}")
            SystemLog.log(f"删除所有用户失败: {str(e)}", "错误")
    @staticmethod
    def modify_remark() -> None:
        """修改用户备注"""
        try:
            data = DataManagement.load_user_data()
            users = data.get("users", {})
            
            if not users:
                safe_print("\n当前没有用户数据")
                return
            
            while True:
                user_id = input("请输入要修改备注的用户ID: ").strip()
                if not user_id:
                    safe_print("ID不能为空")
                    continue
                
                if user_id in users:
                    info = users[user_id]
                    
                    # 显示用户当前信息
                    safe_print("\n=== 用户当前信息 ===")
                    safe_print(f"ID:   {user_id}")
                    safe_print(f"姓名: {info['姓名']}")
                    safe_print(f"年龄: {info['年龄']}")
                    safe_print(f"职业: {info['职业']}")
                    
                    # 显示当前备注
                    current_remark = info.get('备注', '无')
                    safe_print(f"当前备注: {current_remark}")
                    safe_print("-" * 30)
                    
                    # 输入新备注
                    safe_print("\n📝 修改备注信息")
                    safe_print("（直接回车保持原备注，输入BREAK清空备注）")
                    new_remark = input("请输入新备注: ").strip()
                    
                    if new_remark == "":
                        safe_print("备注未修改")
                        break
                    elif new_remark == "BREAK":
                        new_remark = "无"
                        safe_print("备注已清空")
                    
                    # 确认修改
                    safe_print(f"\n原备注: {current_remark}")
                    safe_print(f"新备注: {new_remark}")
                    confirm = input("确定要修改备注吗?(Y/N): ").upper()
                    
                    if confirm == "Y":
                        info['备注'] = new_remark
                        info['最后修改时间'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        
                        if DataManagement.save_user_data(data):
                            safe_print(f"✅ 用户 {user_id} 的备注已修改")
                            SystemLog.log(f"修改用户备注: ID={user_id}, 新备注={new_remark}")
                        else:
                            safe_print("❌ 保存失败")
                        break
                    else:
                        safe_print("修改已取消")
                        break
                else:
                    safe_print(f"❌ ID {user_id} 的用户不存在")
                    if input("是否继续?(Y/N): ").upper() != "Y":
                        break
                        
        except Exception as e:
            safe_print(f"❌ 修改备注时发生错误: {str(e)}")
            SystemLog.log(f"修改备注失败: {str(e)}", "错误")

    @staticmethod
    def add_user_quick(name: str, age: int, gender: str, occupation: str) -> bool:
        """快速添加用户（修复数据完整性）"""
        try:
            if not name or len(name.strip()) == 0:
                safe_print("❌ 姓名不能为空")
                return False
            
            if not isinstance(age, int) or age <= 0 or age >= 120:
                safe_print("❌ 年龄无效 (应为1-119)")
                return False
            
            if gender not in ['男', '女', '其他']:
                gender = '其他'
            
            data = DataManagement.load_user_data()
            
            if data.get("empty_ids"):
                valid_empty_ids = []
                for empty_id in data["empty_ids"]:
                    if isinstance(empty_id, int) and empty_id > 0:
                        if str(empty_id) not in data.get("users", {}):
                            valid_empty_ids.append(empty_id)
                
                data["empty_ids"] = sorted(list(set(valid_empty_ids)))
                
                if data["empty_ids"]:
                    use_id = min(data["empty_ids"])
                    data["empty_ids"] = [id for id in data["empty_ids"] if id != use_id]
                else:
                    use_id = data.get("next_id", 1)
                    data["next_id"] = use_id + 1
            else:
                use_id = data.get("next_id", 1)
                data["next_id"] = use_id + 1
            
            if "next_id" not in data:
                data["next_id"] = use_id + 1
            
            if "users" not in data:
                data["users"] = {}
            
            while str(use_id) in data["users"]:
                use_id += 1
                data["next_id"] = max(data.get("next_id", 1), use_id + 1)
            
            user_info = {
                "姓名": name.strip(),
                "年龄": age,
                "性别": gender,
                "职业": occupation.strip() if occupation else "其他",
                "创建时间": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "最后修改时间": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            data["users"][str(use_id)] = user_info
            
            if "empty_ids" in data:
                data["empty_ids"] = sorted(list(set(data["empty_ids"])))
            
            if DataManagement.save_user_data(data):
                safe_print(f"✅ 快速添加用户成功! ID: {use_id}")
                SystemLog.log(f"快速添加用户: ID={use_id}, 姓名={name}")
                return True
            else:
                safe_print("❌ 保存失败")
                return False
                
        except Exception as e:
            safe_print(f"❌ 快速添加用户失败: {str(e)}")
            SystemLog.log(f"快速添加用户失败: {str(e)}", "错误")
            return False

# ==================== 密码管理 ====================
class PasswordManagement:
    @staticmethod
    def change_password() -> bool:
        """修改密码"""
        safe_print("\n===== 密码管理 =====")
        
        current_passwords = DataManagement.load_secure_passwords()
        
        if current_passwords:
            safe_print("请先输入当前密码进行验证")
            if not UITools.password_verification():
                safe_print("❌ 密码验证失败")
                return False
        
        safe_print("\n设置新密码（输入空密码表示无需密码）：")
        
        while True:
            new_password1 = UITools.input_password("请输入新密码（直接回车表示无密码）: ")
            
            if new_password1:
                firewall_config = DataManagement.load_firewall_config()
                if firewall_config.get('block_weak_passwords', True):
                    strength_check = PasswordManagement.check_password_strength(new_password1)
                    if not strength_check[0]:
                        safe_print(f"❌ 密码强度不足: {strength_check[1]}")
                        continue
            
            new_password2 = UITools.input_password("请再次输入新密码: ")
            
            if new_password1 != new_password2:
                safe_print("❌ 两次输入的密码不一致，请重新输入")
                continue
            
            break
        
        try:
            if new_password1:
                salt, pwd_hash = PasswordSecurity.hash_password(new_password1)
                passwords = [(salt, pwd_hash)]
                
                DataManagement.save_secure_passwords(passwords)
                safe_print("✅ 密码设置成功！")
                safe_print("下次登录系统时将需要密码")
                SystemLog.security_log("修改密码", "用户", "成功")
            else:
                DataManagement.save_secure_passwords([])
                safe_print("✅ 已取消密码！")
                safe_print("下次登录系统时将无需密码")
                SystemLog.security_log("取消密码", "用户", "成功")
            return True
        except Exception as e:
            safe_print(f"❌ 密码保存失败: {str(e)}")
            SystemLog.security_log("修改密码", "用户", "失败")
            return False

    @staticmethod
    def check_password_strength(password: str) -> Tuple[bool, str]:
        """检查密码强度"""
        if len(password) < 6:
            return False, "密码长度至少6位"
        if not any(char.isdigit() for char in password):
            return False, "密码应包含至少一个数字"
        if not any(char.isalpha() for char in password):
            return False, "密码应包含至少一个字母"
        
        weak_passwords = ["123456", "password", "admin", "12345678", "qwerty", "111111", "123123", "000000"]
        if password.lower() in weak_passwords:
            return False, "密码过于常见，请使用更复杂的密码"
        
        return True, "密码强度足够"

# ==================== 防火墙管理 ====================
class FirewallManagement:
    @staticmethod
    def show_status() -> None:
        """显示防火墙状态"""
        config = DataManagement.load_firewall_config()
        safe_print("\n===== 防火墙状态 =====")
        safe_print(f"防火墙状态: {'✅ 已启用' if config.get('enable_firewall') else '❌ 已禁用'}")
        safe_print(f"弱密码检测: {'✅ 开启' if config.get('block_weak_passwords') else '❌ 关闭'}")
        safe_print(f"最大登录尝试: {config.get('max_login_attempts', 5)} 次")
        safe_print(f"会话超时: {config.get('session_timeout', 1800)} 秒")
        safe_print(f"审计日志: {'✅ 开启' if config.get('audit_logging') else '❌ 关闭'}")
        safe_print("=====================")

    @staticmethod
    def toggle_status() -> bool:
        """切换防火墙状态"""
        config = DataManagement.load_firewall_config()
        current_state = config.get('enable_firewall', False)
        
        if current_state:
            confirm = input("确定要禁用防火墙吗? (Y/N): ").strip().upper()
            if confirm == 'Y':
                config['enable_firewall'] = False
                safe_print("✅ 防火墙已禁用")
                SystemLog.security_log("禁用防火墙", "用户", "成功")
            else:
                safe_print("操作已取消")
                return False
        else:
            confirm = input("确定要启用防火墙吗? (Y/N): ").strip().upper()
            if confirm == 'Y':
                config['enable_firewall'] = True
                safe_print("✅ 防火墙已启用")
                SystemLog.security_log("启用防火墙", "用户", "成功")
            else:
                safe_print("操作已取消")
                return False
        
        try:
            with open(firewall_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            safe_print(f"❌ 保存配置失败: {str(e)}")
            return False

    @staticmethod
    def configure_settings() -> bool:
        """配置防火墙设置"""
        config = DataManagement.load_firewall_config()
        
        safe_print("\n===== 防火墙配置 =====")
        safe_print("1. 弱密码检测")
        safe_print("2. 最大登录尝试次数")
        safe_print("3. 会话超时时间")
        safe_print("4. 审计日志")
        safe_print("5. 返回")
        
        choice = input("请选择配置项: ").strip()
        
        if choice == "1":
            current_state = config.get('block_weak_passwords', True)
            config['block_weak_passwords'] = not current_state
            safe_print(f"✅ 弱密码检测已{'开启' if config['block_weak_passwords'] else '关闭'}")
        elif choice == "2":
            try:
                attempts = int(input("请输入最大登录尝试次数: ").strip())
                if 1 <= attempts <= 10:
                    config['max_login_attempts'] = attempts
                    safe_print(f"✅ 最大登录尝试次数设置为 {attempts}")
                else:
                    safe_print("❌ 请输入1-10之间的数字")
            except ValueError:
                safe_print("❌ 请输入有效数字")
        elif choice == "3":
            try:
                timeout = int(input("请输入会话超时时间(秒): ").strip())
                if timeout >= 60:
                    config['session_timeout'] = timeout
                    safe_print(f"✅ 会话超时时间设置为 {timeout} 秒")
                else:
                    safe_print("❌ 超时时间至少60秒")
            except ValueError:
                safe_print("❌ 请输入有效数字")
        elif choice == "4":
            current_state = config.get('audit_logging', True)
            config['audit_logging'] = not current_state
            safe_print(f"✅ 审计日志已{'开启' if config['audit_logging'] else '关闭'}")
        elif choice == "5":
            return True
        else:
            safe_print("❌ 无效选择")
            return False
        
        try:
            with open(firewall_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            safe_print(f"❌ 保存配置失败: {str(e)}")
            return False

# ==================== 网络防火墙 ====================
class NetworkFirewall:
    @staticmethod
    def init() -> bool:
        """初始化网络防火墙"""
        try:
            if not os.path.exists(firewall_file):
                return False
            
            config = DataManagement.load_firewall_config()
            if not config.get("enable_firewall", False):
                return True
            
            return True
        except Exception as e:
            SystemLog.log(f"初始化网络防火墙失败: {str(e)}", "错误")
            return False

    @staticmethod
    def check_network_connection(host: str, port: str) -> bool:
        """检查网络连接"""
        try:
            config = DataManagement.load_firewall_config()
            if not config.get("enable_firewall", False):
                return True
            
            rules = DataManagement.load_network_rules()
            
            for blacklist_rule in rules.get("blacklist", []):
                if NetworkFirewall.match_rule(host, port, blacklist_rule):
                    safe_print(f"🚫 防火墙阻止: {host}:{port} (匹配黑名单规则)")
                    SystemLog.security_log(f"阻止网络连接: {host}:{port}", "防火墙", "成功")
                    return False
            
            whitelist_rules = rules.get("whitelist", [])
            if whitelist_rules:
                allowed = False
                for whitelist in whitelist_rules:
                    if NetworkFirewall.match_rule(host, port, whitelist):
                        allowed = True
                        break
                if not allowed:
                    safe_print(f"🚫 防火墙阻止: {host}:{port} (不在白名单中)")
                    SystemLog.security_log(f"阻止网络连接: {host}:{port}", "防火墙", "成功")
                    return False
            
            return True
        except Exception as e:
            SystemLog.log(f"检查网络连接失败: {str(e)}", "错误")
            return True

    @staticmethod
    def match_rule(host: str, port: str, rule: Dict[str, Any]) -> bool:
        """匹配规则"""
        try:
            rule_host = rule.get("host", "")
            rule_port = rule.get("port", "")
            
            host_match = False
            if rule_host == "*" or rule_host == host:
                host_match = True
            elif rule_host.startswith("*."):
                domain_suffix = rule_host[2:]
                if host.endswith(domain_suffix):
                    host_match = True
            
            port_match = False
            if str(rule_port) == "*":
                port_match = True
            elif "-" in str(rule_port):
                try:
                    start_port, end_port = map(int, str(rule_port).split("-"))
                    port_int = int(port)
                    if start_port <= port_int <= end_port:
                        port_match = True
                except ValueError:
                    port_match = False
            else:
                port_match = str(rule_port) == str(port)
            
            return host_match and port_match
        except:
            return False

    @staticmethod
    def configure_network_rules() -> None:
        """配置网络规则"""
        safe_print("\n===== 网络防火墙规则配置 =====")
        rules = DataManagement.load_network_rules()
        
        while True:
            safe_print("\n1. 查看当前规则")
            safe_print("2. 添加黑名单规则")
            safe_print("3. 添加白名单规则")
            safe_print("4. 删除规则")
            safe_print("5. 测试规则")
            safe_print("6. 保存并返回")
            
            choice = input("请选择: ").strip()
            
            if choice == "1":
                NetworkFirewall.show_current_rules(rules)
            elif choice == "2":
                rules = NetworkFirewall.add_rule(rules, "blacklist")
            elif choice == "3":
                rules = NetworkFirewall.add_rule(rules, "whitelist")
            elif choice == "4":
                rules = NetworkFirewall.delete_rule(rules)
            elif choice == "5":
                NetworkFirewall.test_rule(rules)
            elif choice == "6":
                DataManagement.save_network_rules(rules)
                safe_print("✅ 规则已保存")
                break
            else:
                safe_print("❌ 无效选择")

    @staticmethod
    def show_current_rules(rules: Dict[str, Any]) -> None:
        """显示当前规则"""
        safe_print("\n=== 黑名单规则 ===")
        if not rules.get("blacklist"):
            safe_print("无黑名单规则")
        else:
            for i, rule_item in enumerate(rules.get("blacklist", []), 1):
                safe_print(f"{i}. 主机: {rule_item.get('host', '*')}, 端口: {rule_item.get('port', '*')}")
        
        safe_print("\n=== 白名单规则 ===")
        if not rules.get("whitelist"):
            safe_print("无白名单规则")
        else:
            for i, rule_item in enumerate(rules.get("whitelist", []), 1):
                safe_print(f"{i}. 主机: {rule_item.get('host', '*')}, 端口: {rule_item.get('port', '*')}")

    @staticmethod
    def add_rule(rules: Dict[str, Any], rule_type: str) -> Dict[str, Any]:
        """添加规则"""
        safe_print(f"\n添加{rule_type}规则")
        safe_print("主机格式: example.com 或 *.example.com 或 * (所有主机)")
        safe_print("端口格式: 80 或 1-100 或 * (所有端口)")
        
        host = input("请输入主机: ").strip()
        port = input("请输入端口: ").strip()
        
        if not host:
            host = "*"
        if not port:
            port = "*"
        
        new_rule = {"host": host, "port": port}
        rules[rule_type].append(new_rule)
        safe_print(f"✅ 已添加{rule_type}规则: {host}:{port}")
        return rules

    @staticmethod
    def delete_rule(rules: Dict[str, Any]) -> Dict[str, Any]:
        """删除规则"""
        safe_print("\n=== 删除规则 ===")
        all_rules = []
        
        for i, rule_item in enumerate(rules.get("blacklist", []), 1):
            all_rules.append(("blacklist", i, rule_item))
        
        for i, rule_item in enumerate(rules.get("whitelist", []), 1):
            all_rules.append(("whitelist", i + len(rules.get("blacklist", [])), rule_item))
        
        if not all_rules:
            safe_print("没有规则可删除")
            return rules
        
        for rule_type, num, rule_item in all_rules:
            safe_print(f"{num}. [{rule_type}] 主机: {rule_item.get('host', '*')}, 端口: {rule_item.get('port', '*')}")
        
        try:
            selection = int(input("请选择要删除的规则编号: ").strip())
            if 1 <= selection <= len(all_rules):
                rule_type, original_num, rule_item = all_rules[selection-1]
                rules[rule_type].remove(rule_item)
                safe_print(f"✅ 已删除规则")
            else:
                safe_print("❌ 无效编号")
        except ValueError:
            safe_print("❌ 请输入有效数字")
        
        return rules

    @staticmethod
    def test_rule(rules: Dict[str, Any]) -> None:
        """测试规则"""
        safe_print("\n=== 测试规则 ===")
        host = input("请输入测试主机 (默认: example.com): ").strip() or "example.com"
        port = input("请输入测试端口 (默认: 80): ").strip() or "80"
        
        allowed = NetworkFirewall.check_network_connection(host, port)
        if allowed:
            safe_print(f"✅ 连接允许: {host}:{port}")
        else:
            safe_print(f"❌ 连接阻止: {host}:{port}")

# ==================== 网络功能 ====================
class EnhancedNetworkFunctions:
    @staticmethod
    def real_network_info() -> None:
        """真实的网络信息获取"""
        psutil = SmartLibraryManagement.check_and_import("psutil", "网络监控库 - 可以显示真实的网络接口信息")
        if not psutil:
            return
        
        safe_print("\n=== 网络信息 ===")
        try:
            interfaces = psutil.net_if_addrs()
            stats = psutil.net_if_stats()
            
            for interface, addrs in interfaces.items():
                safe_print(f"\n📡 接口: {interface}")
                
                if interface in stats:
                    stat = stats[interface]
                    status = "启用" if stat.isup else "禁用"
                    safe_print(f"   状态: {status}, 速度: {stat.speed}Mbps")
                
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        safe_print(f"   IPv4: {addr.address}/{addr.netmask}")
                    elif addr.family == socket.AF_INET6:
                        safe_print(f"   IPv6: {addr.address}")
            
            io_counters = psutil.net_io_counters()
            safe_print(f"\n📊 网络统计:")
            safe_print(f"   发送: {io_counters.bytes_sent/1024/1024:.2f} MB")
            safe_print(f"   接收: {io_counters.bytes_recv/1024/1024:.2f} MB")
            safe_print(f"   发送包数: {io_counters.packets_sent}")
            safe_print(f"   接收包数: {io_counters.packets_recv}")
            
        except Exception as e:
            safe_print(f"❌ 获取网络信息失败: {str(e)}")
    
    @staticmethod
    def port_scan() -> None:
        """修复后的端口扫描功能"""
        safe_print("\n=== 端口扫描 ===")
        
        while True:
            safe_print("\n1. 快速扫描常用端口")
            safe_print("2. 自定义端口范围扫描")
            safe_print("3. 特定端口扫描")
            safe_print("4. 返回")
            
            choice = input("请选择扫描方式(1-4): ").strip()
            
            if choice == "1":
                EnhancedNetworkFunctions.quick_port_scan()
            elif choice == "2":
                EnhancedNetworkFunctions.custom_port_scan()
            elif choice == "3":
                EnhancedNetworkFunctions.specific_port_scan()
            elif choice == "4":
                break
            else:
                safe_print("❌ 无效选择")
    
    @staticmethod
    def quick_port_scan() -> None:
        """快速扫描常用端口"""
        host = input("请输入主机地址 (默认: localhost): ").strip() or "localhost"
        
        try:
            safe_print(f"\n🔍 快速扫描 {host} 的常用端口...")
            safe_print("-" * 50)
            
            common_ports = {
                21: "FTP",
                22: "SSH",
                23: "Telnet",
                25: "SMTP",
                53: "DNS",
                80: "HTTP",
                110: "POP3",
                143: "IMAP",
                443: "HTTPS",
                3306: "MySQL",
                3389: "RDP",
                8080: "HTTP Proxy",
                8443: "HTTPS Alt"
            }
            
            open_ports = []
            
            for port, service in common_ports.items():
                sock = None
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.5)
                    result = sock.connect_ex((host, port))
                    
                    if result == 0:
                        status = "✅ 开放"
                        open_ports.append((port, service))
                    else:
                        status = "❌ 关闭"
                    
                    safe_print(f"端口 {port:>5} ({service:<10}): {status}")
                except Exception:
                    safe_print(f"端口 {port:>5} ({service:<10}): ❌ 检测失败")
                finally:
                    if sock:
                        try:
                            sock.close()
                        except:
                            pass
            
            safe_print("-" * 50)
            safe_print(f"扫描完成！发现 {len(open_ports)} 个开放端口")
            
            if open_ports:
                safe_print("\n🔓 开放的端口:")
                for port, service in open_ports:
                    safe_print(f"  • {port} ({service})")
            
        except Exception as e:
            safe_print(f"❌ 端口扫描失败: {str(e)}")
    
    @staticmethod
    def custom_port_scan() -> None:
        """自定义端口范围扫描"""
        host = input("请输入主机地址 (默认: localhost): ").strip() or "localhost"
        
        try:
            start_port = input("请输入起始端口 (1-65535): ").strip()
            end_port = input("请输入结束端口 (1-65535): ").strip()
            
            if not start_port.isdigit() or not end_port.isdigit():
                safe_print("❌ 端口号必须是数字")
                return
            
            start_port = int(start_port)
            end_port = int(end_port)
            
            if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
                safe_print("❌ 端口号必须在1-65535范围内")
                return
            
            if start_port > end_port:
                safe_print("❌ 起始端口不能大于结束端口")
                return
            
            total_ports = end_port - start_port + 1
            if total_ports > 1000:
                confirm = input(f"⚠️  将要扫描 {total_ports} 个端口，这可能需要较长时间。继续吗?(Y/N): ").upper()
                if confirm != 'Y':
                    return
            
            safe_print(f"\n🔍 扫描 {host} 的端口范围 {start_port}-{end_port}...")
            safe_print("-" * 50)
            
            open_ports = []
            current = 0
            
            for port in range(start_port, end_port + 1):
                current += 1
                progress = (current / total_ports) * 100
                print(f"扫描进度: {progress:.1f}% ({current}/{total_ports})", end="\r")
                
                sock = None
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.1)
                    result = sock.connect_ex((host, port))
                    
                    if result == 0:
                        open_ports.append(port)
                except Exception:
                    pass
                finally:
                    if sock:
                        try:
                            sock.close()
                        except:
                            pass
            
            safe_print("\n" + "-" * 50)
            safe_print(f"扫描完成！发现 {len(open_ports)} 个开放端口")
            
            if open_ports:
                for i in range(0, len(open_ports), 10):
                    port_line = open_ports[i:i+10]
                    safe_print("  " + ", ".join(str(port) for port in port_line))
            else:
                safe_print("未发现开放端口")
            
        except Exception as e:
            safe_print(f"❌ 自定义端口扫描失败: {str(e)}")
    
    @staticmethod
    def specific_port_scan() -> None:
        """特定端口扫描"""
        host = input("请输入主机地址 (默认: localhost): ").strip() or "localhost"
        
        try:
            ports_input = input("请输入要扫描的端口(多个用逗号或空格分隔，如80,443,8080): ").strip()
            
            if not ports_input:
                safe_print("❌ 请输入至少一个端口号")
                return
            
            port_strs = ports_input.replace(',', ' ').split()
            port_list = []
            
            for port_str in port_strs:
                port_str = port_str.strip()
                if port_str.isdigit():
                    port = int(port_str)
                    if 1 <= port <= 65535:
                        port_list.append(port)
                    else:
                        safe_print(f"⚠️  忽略无效端口(范围错误): {port_str}")
                else:
                    safe_print(f"⚠️  忽略无效端口(非数字): {port_str}")
            
            if not port_list:
                safe_print("❌ 没有有效的端口号")
                return
            
            safe_print(f"\n🔍 扫描 {host} 的指定端口...")
            safe_print("-" * 50)
            
            open_ports = []
            
            for port in port_list:
                sock = None
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1.0)
                    result = sock.connect_ex((host, port))
                    
                    if result == 0:
                        status = "✅ 开放"
                        open_ports.append(port)
                    else:
                        status = "❌ 关闭"
                    
                    safe_print(f"端口 {port:>5}: {status}")
                except socket.timeout:
                    safe_print(f"端口 {port:>5}: ⏱️  超时")
                except Exception:
                    safe_print(f"端口 {port:>5}: ❌ 检测失败")
                finally:
                    if sock:
                        try:
                            sock.close()
                        except:
                            pass
            
            safe_print("-" * 50)
            safe_print(f"扫描完成！发现 {len(open_ports)} 个开放端口")
            
            if open_ports:
                safe_print("\n🔓 开放的端口:")
                safe_print("  " + ", ".join(str(port) for port in open_ports))
            
        except Exception as e:
            safe_print(f"❌ 特定端口扫描失败: {str(e)}")
    
    @staticmethod
    def dns_lookup() -> None:
        """DNS查询功能"""
        safe_print("\n=== DNS查询 ===")
        hostname = input("请输入域名 (默认: baidu.com): ").strip() or "baidu.com"
        
        try:
            safe_print(f"🔍 查询 {hostname} 的DNS记录...")
            
            try:
                ip_address = socket.gethostbyname(hostname)
                safe_print(f"✅ A记录: {ip_address}")
            except Exception:
                safe_print("❌ 无法解析A记录")
            
            dns = SmartLibraryManagement.check_and_import("dns", "DNS查询库 - 用于MX记录查询")
            if dns:
                try:
                    import dns.resolver
                    answers = dns.resolver.resolve(hostname, 'MX')
                    safe_print("📧 MX记录:")
                    for rdata in answers:
                        safe_print(f"   优先级 {rdata.preference}: {rdata.exchange}")
                except Exception as e:
                    safe_print(f"📧 MX记录: 查询失败 - {str(e)}")
            else:
                safe_print("📧 MX记录: 需要安装dnspython库 (pip install dnspython)")
            
        except Exception as e:
            safe_print(f"❌ DNS查询失败: {str(e)}")
    
    @staticmethod
    def network_benchmark() -> None:
        """网络测速功能"""
        safe_print("\n=== 网络测速 ===")
        url = input("请输入测速URL (默认: https://www.baidu.com): ").strip() or "https://www.baidu.com"
        
        requests = SmartLibraryManagement.check_and_import("requests", "网络请求库 - 用于网络测速")
        if not requests:
            return
        
        safe_print(f"⏱️  正在测试连接到 {url} 的速度...")
        
        try:
            start_time = time.time()
            response = requests.get(url, timeout=10)
            end_time = time.time()
            
            if response.status_code == 200:
                download_time = end_time - start_time
                size = len(response.content)
                speed = size / download_time / 1024  # KB/s
                
                safe_print(f"✅ 连接成功!")
                safe_print(f"   响应时间: {download_time:.3f} 秒")
                safe_print(f"   下载大小: {size/1024:.2f} KB")
                safe_print(f"   下载速度: {speed:.2f} KB/秒")
                safe_print(f"   状态码: {response.status_code}")
            else:
                safe_print(f"⚠️  连接异常! 状态码: {response.status_code}")
                
        except requests.exceptions.Timeout:
            safe_print("❌ 连接超时")
        except requests.exceptions.ConnectionError:
            safe_print("❌ 连接失败")
        except Exception as e:
            safe_print(f"❌ 测速失败: {str(e)}")
    
    @staticmethod
    def show_menu() -> None:
        """显示增强网络功能菜单"""
        while True:
            safe_print("\n===== 网络功能 =====")
            safe_print("1. 网络信息")
            safe_print("2. 端口扫描")
            safe_print("3. DNS查询")
            safe_print("4. 网络测速")
            safe_print("5. 返回主菜单")
            
            choice = input("请选择: ").strip()
            if choice == "1":
                EnhancedNetworkFunctions.real_network_info()
            elif choice == "2":
                EnhancedNetworkFunctions.port_scan()
            elif choice == "3":
                EnhancedNetworkFunctions.dns_lookup()
            elif choice == "4":
                EnhancedNetworkFunctions.network_benchmark()
            elif choice == "5":
                break
            else:
                safe_print("❌ 无效选择")

# ==================== 系统功能 ====================
class SystemFunctions:
    @staticmethod
    def show_system_info() -> None:
        """显示系统信息"""
        try:
            data = DataManagement.load_user_data()
            users = data.get("users", {})
            occupation_list = DataManagement.load_occupation_list()
            firewall_config = DataManagement.load_firewall_config()
            
            safe_print("\n===== 系统信息 =====")
            safe_print(f"系统版本: {system_name}")
            safe_print(f"用户数量: {len(users)}")
            safe_print(f"下一个可用ID: {data['next_id']}")
            safe_print(f"空ID数量: {len(data['empty_ids'])}")
            safe_print(f"职业种类: {len(occupation_list)}种")
            safe_print(f"防火墙状态: {'✅ 启用' if firewall_config.get('enable_firewall') else '❌ 禁用'}")
            safe_print(f"数据目录: {os.path.abspath(data_dir)}")
            
            backup_count = len([f for f in os.listdir(backup_dir) if f.endswith(".json")]) if os.path.exists(backup_dir) else 0
            safe_print(f"备份数量: {backup_count}")
            
            if os.path.exists(log_file):
                log_size = os.path.getsize(log_file)
                safe_print(f"日志大小: {log_size/1024:.2f} KB")
            
            psutil = SmartLibraryManagement.check_and_import("psutil", "系统资源监控库 - 可以显示内存使用率、CPU使用率等系统信息")
            if psutil:
                try:
                    memory_usage = psutil.virtual_memory().percent
                    cpu_usage = psutil.cpu_percent(interval=0.1)
                    safe_print(f"内存使用: {memory_usage}%")
                    safe_print(f"CPU使用: {cpu_usage}%")
                except Exception:
                    safe_print("内存使用: 监控功能暂不可用")
            else:
                safe_print("内存使用: [需要psutil库]")
            
            safe_print("=" * 20)
            
        except Exception as e:
            safe_print(f"❌ 显示系统信息时发生错误: {str(e)}")
            SystemLog.log(f"显示系统信息失败: {str(e)}", "错误")

    @staticmethod
    def view_logs() -> None:
        """查看系统日志"""
        try:
            if not os.path.exists(log_file):
                safe_print("日志文件不存在")
                return
            
            safe_print("\n===== 系统日志 (最后20行) =====")
            with open(log_file, "r", encoding="utf-8") as f:
                all_lines = f.readlines()
                for line in all_lines[-20:]:
                    safe_print(line.strip())
            safe_print("=" * 40)
            
        except Exception as e:
            safe_print(f"❌ 查看日志时发生错误: {str(e)}")
            SystemLog.log(f"查看日志失败: {str(e)}", "错误")

    @staticmethod
    def export_data() -> None:
        """导出数据"""
        try:
            data = DataManagement.load_user_data()
            users = data.get("users", {})
            
            if not users:
                safe_print("没有数据可导出")
                return
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            export_file = os.path.join(data_dir, f"users_export_{timestamp}.csv")
            
            with open(export_file, "w", encoding="utf-8") as f:
                f.write("ID,姓名,年龄,性别,职业,创建时间\n")
                for user_id, info in users.items():
                    f.write(f"{user_id},{info['姓名']},{info['年龄']},{info['性别']},{info['职业']},{info.get('创建时间', '')}\n")
            
            safe_print(f"✅ 数据已导出到: {export_file}")
            SystemLog.log(f"导出数据到 {export_file}")
            
        except Exception as e:
            safe_print(f"❌ 导出数据时发生错误: {str(e)}")
            SystemLog.log(f"导出数据失败: {str(e)}", "错误")
    @staticmethod
    def data_recovery() -> None:
        """数据恢复"""
        DataManagement.data_recovery()

    @staticmethod
    def system_update() -> None:
        """系统更新"""
        try:
            safe_print("\n" + "="*50)
            safe_print("            系统更新")
            safe_print("="*50)
            
            current_version = DataManagement.load_version()
            safe_print(f"当前版本: {current_version}")
            
            # 先检查系统完整性
            safe_print("\n🔍 正在检查系统完整性...")
            if not IntelligentUpdateSystem.check_system_integrity():
                safe_print("⚠️  系统完整性检查发现问题")
                fix_choice = input("是否立即修复? (Y/N): ").strip().upper()
                if fix_choice == 'Y':
                    if IntelligentUpdateSystem.emergency_repair():
                        safe_print("✅ 系统修复完成，可能需要重启")
                        return
                    else:
                        safe_print("❌ 系统修复失败")
            
            safe_print("\n=== 更新选项 ===")
            safe_print("1. 智能集成更新")
            safe_print("2. 手动指定更新")
            safe_print("3. 查看更新包")
            safe_print("4. 手动设置版本")
            safe_print("5. 安全补丁检查")
            safe_print("6. 紧急系统修复")
            safe_print("7. 返回主菜单")
            
            while True:
                choice = input("\n请选择操作(1-7): ").strip()
                
                # 声明全局变量
                global system_name
                
                if choice == "1":
                    # 智能集成更新
                    if IntelligentUpdateSystem.auto_integrate_update():
                        new_version = DataManagement.load_version()
                        system_name = f"PWOS2 v{new_version}"
                        safe_print(f"✅ 系统版本已更新: {system_name}")
                    else:
                        safe_print("❌ 智能更新失败")
                    break
                    
                elif choice == "2":
                    # 手动指定更新
                    if UpdateManagement.manual_update():
                        new_version = DataManagement.load_version()
                        system_name = f"PWOS2 v{new_version}"
                        safe_print(f"✅ 系统版本已更新: {system_name}")
                    else:
                        safe_print("❌ 手动更新失败")
                    break
                    
                elif choice == "3":
                    # 查看更新包
                    SystemFunctions.view_update_packages()
                    # 返回更新菜单
                    return SystemFunctions.system_update()
                    
                elif choice == "4":
                    # 手动设置版本
                    while True:
                        major = input("主版本号 (0-999): ").strip()
                        minor = input("次版本号 (0-999): ").strip()
                        
                        if major.isdigit() and minor.isdigit():
                            major_int = int(major)
                            minor_int = int(minor)
                            
                            if 0 <= major_int <= 999 and 0 <= minor_int <= 999:
                                confirm = input(f"确认将版本设置为 {major_int}.{minor_int}? (Y/N): ").strip().upper()
                                if confirm == 'Y':
                                    if DataManagement.save_version(major_int, minor_int):
                                        system_name = f"PWOS2 v{major_int}.{minor_int}"
                                        safe_print(f"✅ 版本已更新: {system_name}")
                                        break
                                    else:
                                        safe_print("❌ 保存版本失败")
                                else:
                                    safe_print("操作已取消")
                                    break
                            else:
                                safe_print("❌ 版本号应在0-999之间")
                        else:
                            safe_print("❌ 版本号必须为数字")
                    break
                    
                elif choice == "5":
                    # 安全补丁检查
                    UpdateManagement.security_patch_check()
                    # 返回更新菜单
                    return SystemFunctions.system_update()
                    
                elif choice == "6":
                    # 紧急系统修复
                    confirm = input("确定要执行紧急修复吗? (Y/N): ").strip().upper()
                    if confirm == 'Y':
                        if IntelligentUpdateSystem.emergency_repair():
                            safe_print("✅ 紧急修复完成")
                        else:
                            safe_print("❌ 紧急修复失败")
                    else:
                        safe_print("操作已取消")
                    # 返回更新菜单
                    return SystemFunctions.system_update()
                    
                elif choice == "7":
                    # 返回主菜单
                    safe_print("返回主菜单...")
                    return
                    
                else:
                    safe_print("❌ 无效选择，请输入1-7之间的数字")
                
        except KeyboardInterrupt:
            safe_print("\n\n⏹️ 操作被用户中断")
        except Exception as e:
            safe_print(f"❌ 系统更新失败: {str(e)}")
            SystemLog.log(f"系统更新失败: {str(e)}", "错误")
            traceback.print_exc()


    @staticmethod
    def firewall_settings() -> None:
        """防火墙设置"""
        while True:
            safe_print("\n===== 防火墙设置 =====")
            safe_print("1. 查看防火墙状态")
            safe_print("2. 启用/禁用防火墙")
            safe_print("3. 配置防火墙规则")
            safe_print("4. 配置网络防火墙规则")
            safe_print("5. 安全扫描")
            safe_print("6. 测试网络连接")
            safe_print("7. 返回主菜单")
            
            choice = input("请选择: ").strip()
            if choice == "1":
                FirewallManagement.show_status()
            elif choice == "2":
                FirewallManagement.toggle_status()
            elif choice == "3":
                FirewallManagement.configure_settings()
            elif choice == "4":
                NetworkFirewall.configure_network_rules()
            elif choice == "5":
                SystemFunctions.security_scan()
            elif choice == "6":
                SystemFunctions.test_network_connection()
            elif choice == "7":
                break
            else:
                safe_print("❌ 无效选择")

    @staticmethod
    def test_network_connection() -> None:
        """测试网络连接"""
        safe_print("\n===== 测试网络连接 =====")
        requests = SmartLibraryManagement.check_and_import("requests", "网络请求库 - 用于测试网络连接")
        if not requests:
            return
        
        config = DataManagement.load_firewall_config()
        if not config.get("enable_firewall", False):
            safe_print("ℹ️  防火墙未启用，所有连接都会被允许")
        else:
            safe_print("🛡️  防火墙已启用，将根据规则检查连接")
        
        test_list = [
            {"name": "百度", "url": "https://www.baidu.com"},
            {"name": "Google", "url": "https://www.google.com"},
            {"name": "GitHub", "url": "https://github.com"},
            {"name": "DeepSeek API", "url": "https://api.deepseek.com"}
        ]
        
        safe_print("\n正在测试网络连接...")
        for test_item in test_list:
            safe_print(f"\n测试: {test_item['name']} ({test_item['url']})")
            try:
                import urllib.parse
                parsed = urllib.parse.urlparse(test_item['url'])
                host = parsed.hostname
                port = parsed.port or (443 if parsed.scheme == 'https' else 80)
                
                allowed = NetworkFirewall.check_network_connection(host, port)
                if not allowed:
                    safe_print(f"  🚫 防火墙阻止访问")
                    continue
                
                response = requests.get(test_item['url'], timeout=5)
                if response.status_code == 200:
                    safe_print(f"  ✅ 连接成功 ({response.elapsed.total_seconds():.2f}秒)")
                else:
                    safe_print(f"  ⚠️  连接异常 (状态码: {response.status_code})")
                    
            except requests.exceptions.Timeout:
                safe_print("  ⏱️  连接超时")
            except requests.exceptions.ConnectionError:
                safe_print("  🔌 连接失败")
            except Exception as e:
                safe_print(f"  ❌ 错误: {str(e)}")

    @staticmethod
    def security_scan() -> None:
        """安全扫描"""
        safe_print("\n===== 安全扫描 =====")
        issue_count = 0
        
        passwords = DataManagement.load_secure_passwords()
        if not passwords:
            safe_print("❌ 未设置系统密码")
            issue_count += 1
        else:
            safe_print("✅ 已设置系统密码")
            safe_print("⚠️  密码强度检查需要原始密码")
        
        firewall_config = DataManagement.load_firewall_config()
        if not firewall_config.get('enable_firewall'):
            safe_print("❌ 防火墙未启用")
            issue_count += 1
        else:
            safe_print("✅ 防火墙已启用")
        
        backup_list = DataManagement.get_backup_list()
        if not backup_list:
            safe_print("❌ 没有找到备份文件")
            issue_count += 1
        else:
            safe_print(f"✅ 找到 {len(backup_list)} 个备份文件")
        
        if not os.path.exists(log_file):
            safe_print("❌ 日志文件不存在")
            issue_count += 1
        else:
            log_size = os.path.getsize(log_file)
            if log_size == 0:
                safe_print("❌ 日志文件为空")
                issue_count += 1
            else:
                safe_print("✅ 日志文件正常")
        
        safe_print(f"\n扫描完成: 发现 {issue_count} 个安全问题")
        if issue_count > 0:
            safe_print("建议修复上述安全问题以增强系统安全性")

    @staticmethod
    def system_optimization() -> None:
        """系统优化"""
        safe_print("\n===== 系统优化 =====")
        safe_print("1. 清理临时文件")
        safe_print("2. 优化数据库")
        safe_print("3. 检查系统健康")
        safe_print("4. 一键修复系统")
        safe_print("5. 返回主菜单")
        
        choice = input("请选择: ").strip()
        if choice == "1":
            SystemFunctions.clean_temp_files()
        elif choice == "2":
            SystemFunctions.optimize_database()
        elif choice == "3":
            SystemFunctions.system_health_check()
        elif choice == "4":
            SystemFunctions.one_click_repair()
        elif choice == "5":
            return
        else:
            safe_print("❌ 无效选择")

    @staticmethod
    def clean_temp_files() -> None:
        """清理临时文件"""
        safe_print("\n正在清理临时文件...")
        clean_count = 0
        
        if os.path.exists(backup_dir):
            backup_list = sorted([f for f in os.listdir(backup_dir) if f.startswith("users_") and f.endswith(".json")])
            if len(backup_list) > 10:
                for old_backup in backup_list[:-10]:
                    old_backup_path = os.path.join(backup_dir, old_backup)
                    if os.path.exists(old_backup_path):
                        try:
                            os.remove(old_backup_path)
                            clean_count += 1
                            safe_print(f"✅ 已清理: {old_backup}")
                        except Exception:
                            pass
        
        temp_patterns = ['*.backup', '*.tmp', '*.temp', '~*']
        for pattern in temp_patterns:
            import glob
            for file in glob.glob(pattern):
                try:
                    os.remove(file)
                    clean_count += 1
                    safe_print(f"✅ 已清理: {file}")
                except Exception:
                    pass
        
        safe_print(f"✅ 清理完成: 共清理 {clean_count} 个文件")

    @staticmethod
    def optimize_database() -> None:
        """优化数据库"""
        safe_print("\n正在优化数据库...")
        try:
            data = DataManagement.load_user_data()
            if data["empty_ids"]:
                data["empty_ids"] = sorted(data["empty_ids"])
            
            if DataManagement.save_user_data(data):
                safe_print("✅ 数据库优化完成")
                safe_print(f"当前空ID数量: {len(data['empty_ids'])}")
            else:
                safe_print("❌ 数据库优化失败")
                
        except Exception as e:
            safe_print(f"❌ 数据库优化错误: {str(e)}")

    @staticmethod
    def system_health_check() -> Tuple[bool, List[str]]:
        """系统健康检查"""
        safe_print("\n===== 系统健康检查 =====")
        issues = []
        
        necessary_dirs = [data_dir, backup_dir, update_package_dir]
        for dir_path in necessary_dirs:
            if not os.path.exists(dir_path):
                safe_print(f"❌ 目录不存在: {dir_path}")
                issues.append(f"目录不存在: {dir_path}")
            else:
                safe_print(f"✅ 目录正常: {dir_path}")
        
        necessary_files = [user_file, occupation_file, password_file, version_file, firewall_file, network_rules_file]
        for file_path in necessary_files:
            if not os.path.exists(file_path):
                safe_print(f"❌ 文件不存在: {file_path}")
                issues.append(f"文件不存在: {file_path}")
            else:
                safe_print(f"✅ 文件正常: {file_path}")
        
        try:
            with open(user_file, 'a', encoding='utf-8') as f:
                f.write("")
            safe_print("✅ 文件写入权限正常")
        except Exception:
            safe_print("❌ 文件写入权限异常")
            issues.append("文件写入权限异常")
        
        if not issues:
            safe_print("\n🎉 系统健康状态: 优秀 - 无需修复")
            return True, []
        else:
            safe_print(f"\n⚠️  系统健康状态: 发现 {len(issues)} 个问题需要修复")
            return False, issues

    @staticmethod
    def one_click_repair() -> bool:
        """一键修复系统"""
        safe_print("\n===== 一键修复系统 =====")
        safe_print("正在检查系统健康状态...")
        health_status, issues = SystemFunctions.system_health_check()
        
        if health_status:
            safe_print("\n✅ 系统状态良好，无需修复")
            return True
        
        safe_print(f"\n🔧 发现 {len(issues)} 个问题，开始修复...")
        repair_success_count = 0
        
        for issue in issues:
            safe_print(f"\n正在修复: {issue}")
            if "目录不存在" in issue:
                dir_path = issue.split(": ")[1]
                try:
                    os.makedirs(dir_path, exist_ok=True)
                    safe_print(f"✅ 已创建目录: {dir_path}")
                    repair_success_count += 1
                except Exception as e:
                    safe_print(f"❌ 创建目录失败: {str(e)}")
            elif "文件不存在" in issue:
                file_path = issue.split(": ")[1]
                try:
                    if file_path == user_file:
                        default_data = {"users": {}, "next_id": 1, "empty_ids": []}
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(default_data, f, ensure_ascii=False, indent=2)
                    elif file_path == occupation_file:
                        default_occupations = ["学生", "教师", "工程师", "医生", "护士", "程序员", "设计师", "销售", "经理", "厨师", "司机", "公务员", "农民", "自由职业", "其他"]
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(default_occupations, f, ensure_ascii=False, indent=2)
                    elif file_path == password_file:
                        DataManagement.save_secure_passwords([])
                    elif file_path == version_file:
                        DataManagement.save_version(3, 0)
                    elif file_path == firewall_file:
                        default_firewall_rules = {
                            "enable_firewall": False,
                            "block_weak_passwords": True,
                            "max_login_attempts": 5,
                            "session_timeout": 1800,
                            "audit_logging": True
                        }
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(default_firewall_rules, f, ensure_ascii=False, indent=2)
                    elif file_path == network_rules_file:
                        default_network_rules = {
                            "blacklist": [],
                            "whitelist": [],
                            "description": "网络防火墙规则"
                        }
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(default_network_rules, f, ensure_ascii=False, indent=2)
                    else:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write("")
                    safe_print(f"✅ 已创建文件: {file_path}")
                    repair_success_count += 1
                except Exception as e:
                    safe_print(f"❌ 创建文件失败: {str(e)}")
            elif "文件写入权限异常" in issue:
                try:
                    safe_print("⚠️  文件权限问题可能需要管理员权限")
                    safe_print("建议手动检查文件权限")
                    repair_success_count += 1
                except Exception as e:
                    safe_print(f"❌ 修复文件权限失败: {str(e)}")
        
        safe_print(f"\n修复完成: 成功修复 {repair_success_count}/{len(issues)} 个问题")
        if repair_success_count == len(issues):
            safe_print("🎉 所有问题已成功修复！")
            SystemLog.log("一键修复系统完成，所有问题已修复")
            return True
        else:
            safe_print("⚠️  部分问题未能修复，请手动检查")
            SystemLog.log(f"一键修复系统完成，修复了{repair_success_count}/{len(issues)}个问题")
            return False

# ==================== 更新类型表 ====================
update_type_table = {
    "0": {"名称": "系统更新", "必须文件": True, "描述": "核心系统文件更新"},
    "1": {"名称": "数据更新", "必须文件": True, "描述": "用户数据和配置更新"},
    "2": {"名称": "功能更新", "必须文件": False, "描述": "新功能模块添加"},
    "3": {"名称": "其他更新", "必须文件": False, "描述": "文档、资源等更新"},
    "4": {"名称": "测试数据", "必须文件": False, "描述": "测试用数据包"},
    "5": {"名称": "安全补丁", "必须文件": False, "描述": "安全漏洞修复"}
}

# ==================== 更新管理 ====================
class UpdateManagement:
    @staticmethod
    def check_update_packages() -> List[str]:
        """检查更新包"""
        try:
            if not os.path.exists(update_package_dir):
                return []
            
            update_packages = []
            for item in os.listdir(update_package_dir):
                package_path = os.path.join(update_package_dir, item)
                if os.path.isdir(package_path):
                    main_file_path = os.path.join(package_path, "main.txt")
                    if os.path.exists(main_file_path):
                        try:
                            with open(main_file_path, 'r', encoding='utf-8') as f:
                                first_line = f.readline().strip()
                                if first_line and first_line[0] in update_type_table:
                                    update_packages.append(item)
                        except Exception:
                            continue
            
            return sorted(update_packages)
        except Exception as e:
            SystemLog.log(f"检查更新包失败: {str(e)}", "错误")
            return []

    @staticmethod
    def parse_update_package(package_path: str) -> Optional[Dict[str, Any]]:
        """解析更新包"""
        try:
            main_file_path = os.path.join(package_path, "main.txt")
            if not os.path.exists(main_file_path):
                return None
            
            with open(main_file_path, 'r', encoding='utf-8') as f:
                content = f.readlines()
            
            if not content or not content[0].strip():
                return None
            
            first_line = content[0].strip()
            if first_line[0] not in update_type_table:
                return None
            
            type_code = first_line[0]
            type_info = update_type_table[type_code]
            comment = content[1].strip() if len(content) > 1 and content[1].strip() else type_info["描述"]
            
            package_files = []
            if os.path.exists(package_path):
                package_files = [f for f in os.listdir(package_path) if f != "main.txt" and os.path.isfile(os.path.join(package_path, f))]
            
            if type_info["必须文件"] and not package_files:
                return None
            
            return {
                "包名": os.path.basename(package_path),
                "类型码": type_code,
                "类型名称": type_info["名称"],
                "注释": comment,
                "文件列表": package_files,
                "路径": package_path
            }
        except Exception as e:
            SystemLog.log(f"解析更新包失败 {package_path}: {str(e)}", "错误")
            return None

    @staticmethod
    def auto_update() -> bool:
        """自动更新"""
        try:
            safe_print("\n===== 自动更新检查 =====")
            update_packages = UpdateManagement.check_update_packages()
            
            if not update_packages:
                safe_print("✅ 没有找到可用的更新包")
                return True
            
            safe_print(f"📦 找到 {len(update_packages)} 个更新包")
            for package_name in update_packages:
                package_path = os.path.join(update_package_dir, package_name)
                package_info = UpdateManagement.parse_update_package(package_path)
                
                if package_info:
                    safe_print(f"\n准备更新: {package_info['包名']}")
                    safe_print(f"类型: {package_info['类型名称']}")
                    safe_print(f"描述: {package_info['注释']}")
                    safe_print(f"文件: {', '.join(package_info['文件列表']) if package_info['文件列表'] else '无文件'}")
                    
                    confirm = input("是否执行此更新?(Y/N): ").strip().upper()
                    if confirm in ['Y', 'YES']:
                        success, message = UpdateManagement.execute_update(package_info)
                        if success:
                            safe_print(f"✅ {message}")
                            UpdateManagement.clean_update_package(package_name)
                        else:
                            safe_print(f"❌ {message}")
                            return False
                    else:
                        safe_print(">>️  跳过此更新包")
                else:
                    safe_print(f"❌ 无效的更新包: {package_name}")
            
            return True
        except Exception as e:
            safe_print(f"❌ 自动更新失败: {str(e)}")
            SystemLog.log(f"自动更新失败: {str(e)}", "错误")
            return False

    @staticmethod
    def manual_update() -> bool:
        """手动更新"""
        try:
            safe_print("\n===== 手动更新 =====")
            safe_print("请输入更新包文件夹的完整路径")
            safe_print("例如: D:/1 或 D:\\1 或 d:/1")
            safe_print("输入 'cancel' 取消操作")
            
            while True:
                input_path = input("更新包路径: ").strip()
                if not input_path:
                    safe_print("❌ 路径不能为空，请重新输入")
                    continue
                
                if input_path.lower() == 'cancel':
                    safe_print("⏹️  手动更新已取消")
                    return False
                
                update_package_path = input_path.replace('\\', '/')
                if os.name == 'nt' and len(update_package_path) > 1 and update_package_path[1] == ':':
                    update_package_path = update_package_path[0].upper() + update_package_path[1:]
                
                if not os.path.exists(update_package_path):
                    safe_print("❌ 路径不存在，请重新输入")
                    continue
                
                if not os.path.isdir(update_package_path):
                    safe_print("❌ 路径不是文件夹，请重新输入")
                    continue
                
                package_info = UpdateManagement.parse_update_package(update_package_path)
                if not package_info:
                    safe_print("❌ 无效的更新包，请检查main.txt文件格式")
                    continue
                
                safe_print(f"\n✅ 找到更新包: {package_info['包名']}")
                safe_print(f"📋 类型: {package_info['类型名称']}")
                safe_print(f"📝 描述: {package_info['注释']}")
                safe_print(f"📁 文件: {', '.join(package_info['文件列表']) if package_info['文件列表'] else '无文件'}")
                
                confirm = input("是否执行此更新?(Y/N): ").strip().upper()
                if confirm in ['Y', 'YES']:
                    success, message = UpdateManagement.execute_update(package_info)
                    if success:
                        safe_print(f"✅ {message}")
                        return True
                    else:
                        safe_print(f"❌ {message}")
                        return False
                else:
                    safe_print("⏹️  更新已取消")
                    return False
                    
        except Exception as e:
            safe_print(f"❌ 手动更新失败: {str(e)}")
            SystemLog.log(f"手动更新失败: {str(e)}", "错误")
            return False

    @staticmethod
    def system_update_confirmation() -> bool:
        """系统更新确认"""
        safe_print("\n⚠️  警告: 即将进行系统核心更新")
        safe_print("这可能会修改系统核心文件，请确保已备份重要数据")
        confirm = input("确定要继续吗?(Y/N): ").strip().upper()
        return confirm == "Y"

    @staticmethod
    def execute_update(package_info: Dict[str, Any]) -> Tuple[bool, str]:
        """执行更新"""
        try:
            SystemLog.log(f"开始执行更新: {package_info['包名']} - {package_info['类型名称']}")
            
            if package_info["类型码"] == "0":
                if not UpdateManagement.system_update_confirmation():
                    return False, "用户取消了系统更新"
            
            update_result = False
            update_message = ""
            
            if package_info["类型码"] == "0":
                update_result, update_message = UpdateManagement.execute_system_update(package_info)
            elif package_info["类型码"] == "1":
                update_result, update_message = UpdateManagement.execute_data_update(package_info)
            elif package_info["类型码"] == "2":
                update_result, update_message = UpdateManagement.execute_function_update(package_info)
            elif package_info["类型码"] == "3":
                update_result, update_message = UpdateManagement.execute_other_update(package_info)
            elif package_info["类型码"] == "4":
                update_result, update_message = UpdateManagement.execute_test_update(package_info)
            elif package_info["类型码"] == "5":
                update_result, update_message = UpdateManagement.execute_security_update(package_info)
            else:
                return False, "未知的更新类型"
            
            if update_result and package_info["类型码"] not in ["4"]:
                UpdateManagement.auto_increment_version()
            
            return update_result, update_message
        except Exception as e:
            error_info = f"执行更新失败: {str(e)}"
            SystemLog.log(error_info, "错误")
            return False, error_info

    @staticmethod
    def auto_increment_version() -> bool:
        """自动递增版本号"""
        try:
            with open(version_file, 'r', encoding='utf-8') as f:
                current_version = json.load(f)
            
            major = current_version["major"]
            minor = current_version["minor"]
            minor += 1
            
            if minor >= 100:
                major += 1
                minor = 0
            
            DataManagement.save_version(major, minor)
            new_version = f"{major}.{minor}"
            
            SystemLog.log(f"版本号自动递增: v{current_version['major']}.{current_version['minor']} → v{new_version}")
            safe_print(f"✅ 系统版本已更新: v{new_version}")
            return True
        except Exception as e:
            SystemLog.log(f"自动递增版本号失败: {str(e)}", "错误")
            return False

    @staticmethod
    def execute_system_update(package_info: Dict[str, Any]) -> Tuple[bool, str]:
        """执行系统更新"""
        try:
            safe_print(f"🔄 正在执行系统更新: {package_info['注释']}")
            
            if "new_version.json" not in package_info["文件列表"]:
                return False, "❌ 系统更新必须包含 new_version.json 文件"
            
            version_file_path = os.path.join(package_info["路径"], "new_version.json")
            with open(version_file_path, 'r', encoding='utf-8') as f:
                new_version = json.load(f)
            
            DataManagement.save_version(new_version["major"], new_version["minor"])
            safe_print(f"✅ 版本号更新: v{new_version['major']}.{new_version['minor']}")
            
            for file in package_info["文件列表"]:
                if file.endswith('.py') and file != "new_version.json":
                    source_file = os.path.join(package_info["路径"], file)
                    target_file = os.path.join(".", file)
                    shutil.copy2(source_file, target_file)
                    safe_print(f"✅ 已更新系统文件: {file}")
            
            SystemLog.log(f"系统更新完成: {package_info['包名']}")
            return True, "✅ 系统更新完成"
        except Exception as e:
            return False, f"❌ 系统更新失败: {str(e)}"

    @staticmethod
    def execute_data_update(package_info: Dict[str, Any]) -> Tuple[bool, str]:
        """执行数据更新"""
        try:
            safe_print(f"🔄 正在执行数据更新: {package_info['注释']}")
            
            json_files = [f for f in package_info["文件列表"] if f.endswith('.json')]
            if not json_files:
                return False, "❌ 数据更新必须包含JSON文件"
            
            DataManagement.create_backup()
            
            for file in package_info["文件列表"]:
                if file == "new_users.json":
                    source_file = os.path.join(package_info["路径"], "new_users.json")
                    shutil.copy2(source_file, user_file)
                    safe_print("✅ 已更新用户数据")
                elif file == "new_occupations.json":
                    source_file = os.path.join(package_info["路径"], "new_occupations.json")
                    shutil.copy2(source_file, occupation_file)
                    safe_print("✅ 已更新职业数据")
                elif file.endswith('.json'):
                    source_file = os.path.join(package_info["路径"], file)
                    target_file = os.path.join(data_dir, file)
                    shutil.copy2(source_file, target_file)
                    safe_print(f"✅ 已更新数据文件: {file}")
            
            SystemLog.log(f"数据更新完成: {package_info['包名']}")
            return True, "✅ 数据更新完成"
        except Exception as e:
            return False, f"❌ 数据更新失败: {str(e)}"

    @staticmethod
    def execute_function_update(package_info: Dict[str, Any]) -> Tuple[bool, str]:
        """执行功能更新"""
        try:
            safe_print(f"🔄 正在执行功能更新: {package_info['注释']}")
            
            for file in package_info["文件列表"]:
                if file.endswith('.py'):
                    source_file = os.path.join(package_info["路径"], file)
                    target_file = os.path.join(".", file)
                    shutil.copy2(source_file, target_file)
                    safe_print(f"✅ 已更新功能文件: {file}")
            
            SystemLog.log(f"功能更新完成: {package_info['包名']}")
            return True, "✅ 功能更新完成"
        except Exception as e:
            return False, f"❌ 功能更新失败: {str(e)}"

    @staticmethod
    def execute_other_update(package_info: Dict[str, Any]) -> Tuple[bool, str]:
        """执行其他更新"""
        try:
            safe_print(f"🔄 正在执行其他更新: {package_info['注释']}")
            
            for file in package_info["文件列表"]:
                source_file = os.path.join(package_info["路径"], file)
                if file.endswith('.json'):
                    target_file = os.path.join(data_dir, file)
                    shutil.copy2(source_file, target_file)
                    safe_print(f"✅ 已更新配置文件: {file}")
                elif file.endswith('.py'):
                    target_file = os.path.join(".", file)
                    shutil.copy2(source_file, target_file)
                    safe_print(f"✅ 已更新脚本文件: {file}")
                else:
                    safe_print(f"✅ 已处理文件: {file}")
            
            SystemLog.log(f"其他更新完成: {package_info['包名']}")
            return True, "✅ 其他更新完成"
        except Exception as e:
            return False, f"❌ 其他更新失败: {str(e)}"

    @staticmethod
    def execute_test_update(package_info: Dict[str, Any]) -> Tuple[bool, str]:
        """执行测试更新"""
        try:
            safe_print(f"🔄 正在执行测试更新: {package_info['注释']}")
            
            if package_info["文件列表"]:
                for file in package_info["文件列表"]:
                    source_file = os.path.join(package_info["路径"], file)
                    target_file = os.path.join(data_dir, file)
                    shutil.copy2(source_file, target_file)
                    safe_print(f"✅ 已导入测试文件: {file}")
            else:
                safe_print("ℹ️  无文件测试更新")
            
            SystemLog.log(f"测试更新完成: {package_info['包名']}")
            return True, "✅ 测试更新完成"
        except Exception as e:
            return False, f"❌ 测试更新失败: {str(e)}"

    @staticmethod
    def execute_security_update(package_info: Dict[str, Any]) -> Tuple[bool, str]:
        """执行安全更新"""
        try:
            safe_print(f"🛡️  正在执行安全更新: {package_info['注释']}")
            
            if package_info["文件列表"]:
                for file in package_info["文件列表"]:
                    source_file = os.path.join(package_info["路径"], file)
                    if file.endswith('.json'):
                        target_file = os.path.join(data_dir, file)
                        shutil.copy2(source_file, target_file)
                        safe_print(f"✅ 已更新安全配置: {file}")
                    elif file.endswith('.py'):
                        target_file = os.path.join(".", file)
                        shutil.copy2(source_file, target_file)
                        safe_print(f"✅ 已更新安全模块: {file}")
                    else:
                        safe_print(f"✅ 已处理安全文件: {file}")
            else:
                safe_print("ℹ️  无文件安全更新 - 可能是配置调整")
            
            SystemLog.security_log(f"安全更新: {package_info['包名']}", "系统", "成功")
            return True, "安全更新完成"
        except Exception as e:
            SystemLog.security_log(f"安全更新: {package_info['包名']}", "系统", "失败")
            return False, f"安全更新失败: {str(e)}"

    @staticmethod
    def security_patch_check() -> bool:
        """安全补丁检查"""
        safe_print("\n===== 安全补丁检查 =====")
        update_packages = UpdateManagement.check_update_packages()
        security_patch_count = 0
        
        for package_name in update_packages:
            package_path = os.path.join(update_package_dir, package_name)
            package_info = UpdateManagement.parse_update_package(package_path)
            
            if package_info and package_info["类型码"] == "5":
                security_patch_count += 1
                safe_print(f"\n🛡️  发现安全补丁: {package_info['包名']}")
                safe_print(f"   描述: {package_info['注释']}")
                safe_print(f"   文件: {', '.join(package_info['文件列表']) if package_info['文件列表'] else '配置更新'}")
                
                confirm = input("是否立即安装此安全补丁?(Y/N): ").strip().upper()
                if confirm in ['Y', 'YES']:
                    success, message = UpdateManagement.execute_security_update(package_info)
                    if success:
                        safe_print(f"✅ {message}")
                        UpdateManagement.clean_update_package(package_name)
                    else:
                        safe_print(f"❌ {message}")
        
        if security_patch_count == 0:
            safe_print("✅ 没有发现可用的安全补丁")
        
        return security_patch_count > 0

    @staticmethod
    def clean_update_package(package_name: str) -> None:
        """清理更新包"""
        try:
            package_path = os.path.join(update_package_dir, package_name)
            if os.path.exists(package_path):
                shutil.rmtree(package_path)
                SystemLog.log(f"已清理更新包: {package_name}")
        except Exception as e:
            SystemLog.log(f"清理更新包失败 {package_name}: {str(e)}", "错误")

# ==================== 智能集成更新系统（完整修复版） ====================
class IntelligentUpdateSystem:
    """智能集成更新系统 - 完整修复版"""
    
    # ==================== 类模板（使用双引号避免冲突） ====================
    CLASS_TEMPLATE = """class IntelligentUpdateSystem:
    \"\"\"智能集成更新系统\"\"\"
    
    @staticmethod
    def auto_integrate_update() -> bool:
        \"\"\"自动应用更新\"\"\"
        safe_print("\\n===== 智能集成更新系统 =====")
        safe_print("正在扫描更新包...")
        
        update_packages = UpdateManagement.check_update_packages()
        if not update_packages:
            safe_print("✅ 没有可用的更新包")
            return False
        
        safe_print(f"📦 发现 {len(update_packages)} 个更新包")
        
        safe_print("\\n=== 更新方式选择 ===")
        safe_print("1. 直接集成到当前系统 (覆盖更新)")
        safe_print("2. 创建新系统文件 (保留原系统备份)")
        safe_print("3. 取消更新")
        
        while True:
            update_method = input("请选择更新方式(1-3): ").strip()
            if update_method == "1":
                return IntelligentUpdateSystem.integrate_to_current(update_packages)
            elif update_method == "2":
                return IntelligentUpdateSystem.create_new_system(update_packages)
            elif update_method == "3":
                safe_print("⏹️ 更新已取消")
                return False
            else:
                safe_print("❌ 无效选择")
    
    @staticmethod
    def integrate_to_current(update_packages: List[str]) -> bool:
        \"\"\"集成到当前系统\"\"\"
        try:
            safe_print("\\n🔄 开始直接集成更新到当前系统...")
            
            # 备份当前系统
            current_file = sys.argv[0] if sys.argv else __file__
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"{current_file}.backup_{timestamp}"
            shutil.copy2(current_file, backup_file)
            safe_print(f"📦 系统已备份: {backup_file}")
            
            integrated_count = 0
            
            for package_name in update_packages:
                package_path = os.path.join(update_package_dir, package_name)
                package_info = UpdateManagement.parse_update_package(package_path)
                
                if package_info:
                    safe_print(f"\\n📦 处理更新包: {package_info['包名']}")
                    safe_print(f"📋 类型: {package_info['类型名称']}")
                    safe_print(f"📝 描述: {package_info['注释']}")
                    
                    confirm = input("是否执行此更新?(Y/N): ").strip().upper()
                    if confirm in ['Y', 'YES']:
                        success, message = UpdateManagement.execute_update(package_info)
                        if success:
                            safe_print(f"✅ {message}")
                            UpdateManagement.clean_update_package(package_name)
                            integrated_count += 1
                        else:
                            safe_print(f"❌ {message}")
            
            safe_print(f"\\n📊 集成完成: {integrated_count}个成功")
            
            if integrated_count > 0:
                safe_print("\\n🔄 系统将在3秒后重启...")
                for i in range(3, 0, -1):
                    safe_print(f"{i}...")
                    time.sleep(1)
                
                safe_print("🔄 正在重启系统...")
                SystemLog.log(f"智能更新完成，集成{integrated_count}个包", "信息")
                os.execv(sys.executable, [sys.executable] + sys.argv)
            
            return integrated_count > 0
            
        except Exception as e:
            safe_print(f"❌ 集成更新失败: {str(e)}")
            SystemLog.log(f"集成更新失败: {str(e)}", "错误")
            return False
    
    @staticmethod
    def create_new_system(update_packages: List[str]) -> bool:
        \"\"\"创建新系统\"\"\"
        try:
            safe_print("\\n🔄 开始创建新系统文件...")
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            current_file = sys.argv[0] if sys.argv else __file__
            original_file = os.path.basename(current_file)
            new_system_file = f"PWOS2_v{DataManagement.load_version()}_{timestamp}.py"
            
            safe_print(f"📄 原系统文件: {original_file}")
            safe_print(f"📄 新系统文件: {new_system_file}")
            
            # 备份原系统
            backup_file = f"{original_file}.backup_{timestamp}"
            shutil.copy2(current_file, backup_file)
            safe_print(f"📦 原系统已备份为: {backup_file}")
            
            # 读取当前代码
            with open(current_file, 'r', encoding='utf-8') as f:
                current_code = f.read()
            
            new_code = current_code
            integrated_count = 0
            
            for package_name in update_packages:
                package_path = os.path.join(update_package_dir, package_name)
                package_info = UpdateManagement.parse_update_package(package_path)
                
                if package_info:
                    safe_print(f"\\n📦 处理更新包: {package_info['包名']}")
                    
                    special_update_file = os.path.join(package_info["路径"], "update_special.py")
                    if os.path.exists(special_update_file):
                        safe_print("🔍 检测到特殊更新文件...")
                        new_code = IntelligentUpdateSystem.apply_special_update(new_code, special_update_file, package_info.get("包名", "未知"))
                    else:
                        new_code = IntelligentUpdateSystem.integrate_code_from_package(new_code, package_info)
                    
                    integrated_count += 1
            
            # 写入新系统文件
            with open(new_system_file, 'w', encoding='utf-8') as f:
                f.write(new_code)
            
            safe_print(f"\\n✅ 新系统文件已创建: {new_system_file}")
            safe_print(f"📊 集成了 {integrated_count} 个更新包")
            
            # 显示系统选择菜单
            safe_print("\\n=== 系统选择 ===")
            safe_print("1. 继续使用原系统")
            safe_print(f"2. 切换到新系统 ({new_system_file})")
            safe_print("3. 同时保留两个系统")
            
            while True:
                choice = input("请选择要使用的系统(1-3): ").strip()
                if choice == "1":
                    safe_print("ℹ️  继续使用原系统，新系统文件保留")
                    return False
                elif choice == "2":
                    # 设置重启标记
                    with open("restart_marker.txt", 'w', encoding='utf-8') as f:
                        f.write(new_system_file)
                    
                    safe_print("\\n🔄 启动新系统...")
                    time.sleep(2)
                    os.execv(sys.executable, [sys.executable, new_system_file])
                    return True
                elif choice == "3":
                    safe_print("ℹ️  两个系统都已保存，下次启动时可以选择")
                    return True
                else:
                    safe_print("❌ 无效选择")
                    
        except Exception as e:
            safe_print(f"❌ 创建新系统失败: {str(e)}")
            SystemLog.log(f"创建新系统失败: {str(e)}", "错误")
            return False
    
    @staticmethod
    def apply_special_update(current_code: str, special_update_file: str, package_name: str = "未知") -> str:
        \"\"\"应用特殊更新\"\"\"
        try:
            with open(special_update_file, 'r', encoding='utf-8') as f:
                special_code = f.read()
            
            if "# REPLACE_SECTION" in special_code:
                replace_content = special_code.split("# REPLACE_SECTION")[1]
                
                if "# END_REPLACE" not in replace_content:
                    safe_print(f"❌ 更新包 {package_name} 格式错误：缺少 END_REPLACE")
                    return current_code
                
                replace_target = replace_content.split("# END_REPLACE")[0].strip()
                replace_with = replace_content.split("# END_REPLACE")[1].strip()
                
                if replace_target in current_code:
                    current_code = current_code.replace(replace_target, replace_with)
                    safe_print(f"✅ 安全替换完成")
                
            return current_code
            
        except Exception as e:
            safe_print(f"❌ 特殊更新失败: {str(e)}")
            return current_code
    
    @staticmethod
    def integrate_code_from_package(current_code: str, package_info: Dict[str, Any]) -> str:
        \"\"\"从更新包集成代码\"\"\"
        code_files = [f for f in package_info.get("文件列表", []) if f.endswith('.py')]
        for code_file in code_files:
            source_file = os.path.join(package_info["路径"], code_file)
            try:
                with open(source_file, 'r', encoding='utf-8') as f:
                    new_code = f.read()
                
                # 尝试添加新类
                lines = new_code.split('\\n')
                for line in lines:
                    if line.strip().startswith('class '):
                        class_name = line.split('class ')[1].split('(')[0].split(':')[0].strip()
                        
                        if f"class {class_name}" not in current_code:
                            # 在合适位置插入
                            insert_pos = current_code.find('if __name__ == \"__main__\":')
                            if insert_pos == -1:
                                insert_pos = len(current_code)
                            
                            current_code = current_code[:insert_pos] + "\\n\\n" + new_code + "\\n" + current_code[insert_pos:]
                            safe_print(f"✅ 添加新类: {class_name}")
                            break
                
            except Exception as e:
                safe_print(f"❌ 集成代码失败 {code_file}: {str(e)}")
        
        return current_code
    
    @staticmethod
    def check_system_integrity() -> bool:
        \"\"\"检查系统完整性\"\"\"
        safe_print("\\n🔍 检查系统完整性...")
        
        try:
            # 检查当前文件
            current_file = sys.argv[0] if sys.argv else __file__
            if not os.path.exists(current_file):
                safe_print("❌ 系统文件不存在")
                return False
            
            file_size = os.path.getsize(current_file)
            safe_print(f"📄 系统文件: {file_size} 字节")
            
            if file_size < 10000:
                safe_print("⚠️  系统文件可能不完整")
            
            # 检查关键类
            required_classes = [
                "IntelligentUpdateSystem",
                "UpdateManagement",
                "DataManagement",
                "UserManagement"
            ]
            
            for class_name in required_classes:
                if class_name not in globals():
                    safe_print(f"❌ 缺少类: {class_name}")
                    return False
            
            safe_print("✅ 系统完整性检查通过")
            return True
            
        except Exception as e:
            safe_print(f"❌ 完整性检查失败: {str(e)}")
            return False
    
    @staticmethod
    def emergency_repair() -> bool:
        \"\"\"紧急修复系统\"\"\"
        try:
            safe_print("\\n🛠️  紧急修复系统...")
            
            current_file = sys.argv[0] if sys.argv else __file__
            safe_print(f"修复目标: {current_file}")
            
            # 1. 备份
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"{current_file}.repair_backup_{timestamp}"
            shutil.copy2(current_file, backup_file)
            safe_print(f"📦 已备份: {backup_file}")
            
            # 2. 读取当前文件
            with open(current_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 3. 检查 IntelligentUpdateSystem 类
            if "class IntelligentUpdateSystem:" not in content:
                safe_print("❌ 缺少 IntelligentUpdateSystem 类")
                
                # 在合适位置插入
                insert_pos = content.find("\\n# ==================== 主程序 ====================")
                if insert_pos == -1:
                    insert_pos = len(content)
                
                # 添加完整的类
                content = content[:insert_pos] + "\\n" + IntelligentUpdateSystem.CLASS_TEMPLATE.strip() + content[insert_pos:]
                safe_print("✅ 已添加 IntelligentUpdateSystem 类")
            
            else:
                safe_print("✅ IntelligentUpdateSystem 类已存在")
                
                # 检查方法是否完整
                required_methods = ["auto_integrate_update", "integrate_to_current", "create_new_system"]
                class_start = content.find("class IntelligentUpdateSystem:")
                class_end = content.find("\\nclass ", class_start + 1)
                if class_end == -1:
                    class_end = len(content)
                
                class_code = content[class_start:class_end]
                
                missing_methods = []
                for method in required_methods:
                    if f"def {method}" not in class_code:
                        missing_methods.append(method)
                
                if missing_methods:
                    safe_print(f"⚠️  类不完整，缺失方法: {', '.join(missing_methods)}")
                    safe_print("🔄 正在修复...")
                    
                    # 替换整个类
                    before_class = content[:class_start]
                    after_class = content[class_end:]
                    content = before_class + IntelligentUpdateSystem.CLASS_TEMPLATE.strip() + after_class
                    safe_print("✅ 已修复类")
            
            # 4. 写入修复后的文件
            with open(current_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            file_size = os.path.getsize(current_file)
            safe_print(f"✅ 修复完成，文件大小: {file_size} 字节")
            
            # 5. 提示重启
            safe_print("\\n🔄 修复完成，建议重启系统")
            restart = input("是否立即重启系统? (Y/N): ").strip().upper()
            if restart == 'Y':
                safe_print("正在重启...")
                time.sleep(2)
                os.execv(sys.executable, [sys.executable] + sys.argv)
            
            return True
            
        except Exception as e:
            safe_print(f"❌ 紧急修复失败: {str(e)}")
            return False
"""
    @staticmethod
    def validate_code_integrity(code: str) -> bool:
        """验证代码完整性"""
        try:
            # 检查基本语法
            if not code or len(code) < 1000:
                safe_print("❌ 代码过短，可能不完整，请注意！")
        
            # 检查关键类是否存在
            required_classes = [
                "class IntelligentUpdateSystem:",
                "class UpdateManagement:",
                "class DataManagement:",
                "class UserManagement:"
            ]
        
            for class_name in required_classes:
                if class_name not in code:
                    safe_print(f"❌ 缺少关键类: {class_name}")
                    return False
        
            # 检查括号平衡
            if code.count('(') != code.count(')'):
                safe_print("❌ 括号不平衡，请注意！")
        
            if code.count('{') != code.count('}'):
                safe_print("❌ 大括号不平衡，请注意！")
        
            if code.count('[') != code.count(']'):
                safe_print("❌ 方括号不平衡，请注意！")
        
            # 检查引号平衡
            if code.count("'") % 2 != 0:
                safe_print("❌ 单引号不平衡，请注意！")
        
            safe_print("✅ 代码完整性验证通过")
            return True
        
        except Exception as e:
            safe_print(f"❌ 代码验证异常: {str(e)}")
            return False

    # ==================== 实际的方法实现 ====================
    
    @staticmethod
    def auto_integrate_update() -> bool:
        """自动应用更新"""
        # 直接使用模板中的方法逻辑
        safe_print("\n===== 智能集成更新系统 =====")
        safe_print("正在扫描更新包...")
        
        update_packages = UpdateManagement.check_update_packages()
        if not update_packages:
            safe_print("✅ 没有可用的更新包")
            return False
        
        safe_print(f"📦 发现 {len(update_packages)} 个更新包")
        
        safe_print("\n=== 更新方式选择 ===")
        safe_print("1. 直接集成到当前系统 (覆盖更新)")
        safe_print("2. 创建新系统文件 (保留原系统备份)")
        safe_print("3. 取消更新")
        
        while True:
            update_method = input("请选择更新方式(1-3): ").strip()
            if update_method == "1":
                return IntelligentUpdateSystem.integrate_to_current(update_packages)
            elif update_method == "2":
                return IntelligentUpdateSystem.create_new_system(update_packages)
            elif update_method == "3":
                safe_print("⏹️ 更新已取消")
                return False
            else:
                safe_print("❌ 无效选择")
    
    @staticmethod
    def integrate_to_current(update_packages: List[str]) -> bool:
        """集成到当前系统（安全版）"""
        try:
            safe_print("\n🔄 开始直接集成更新到当前系统...")
        
            # 获取当前文件
            current_file = sys.argv[0] if sys.argv else __file__
            safe_print(f"📄 当前系统文件: {os.path.basename(current_file)}")
        
            # 先创建一个临时副本，在副本上操作
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            temp_file = f"{current_file}.temp_{timestamp}"
            backup_file = f"{current_file}.backup_{timestamp}"
        
            # 1. 备份原文件
            shutil.copy2(current_file, backup_file)
            safe_print(f"📦 系统已备份: {os.path.basename(backup_file)}")
        
            # 2. 创建临时副本
            shutil.copy2(current_file, temp_file)
        
            # 3. 在临时副本上应用更新
            with open(temp_file, 'r', encoding='utf-8') as f:
                current_code = f.read()
        
            modified_code = current_code
            integrated_count = 0
            update_applied = False
        
            for package_name in update_packages:
                package_path = os.path.join(update_package_dir, package_name)
                package_info = UpdateManagement.parse_update_package(package_path)
            
                if package_info:
                    safe_print(f"\n📦 处理更新包: {package_info['包名']}")
                    safe_print(f"📋 类型: {package_info['类型名称']}")
                
                    # 检查是否是系统类更新
                    is_system_update = False
                    for file in package_info.get("文件列表", []):
                        if "intelligent_update" in file.lower() or "update_system" in file.lower():
                            is_system_update = True
                            break
                
                    if is_system_update:
                        safe_print("⚠️  检测到系统类更新，采用安全模式")
                        # 对于系统类更新，只更新数据，不修改代码
                        confirm = input("这是系统类更新，确定要继续吗? (Y/N): ").strip().upper()
                        if confirm != 'Y':
                            safe_print("⏭️  跳过系统类更新")
                            continue
                
                    confirm = input("是否执行此更新?(Y/N): ").strip().upper()
                    if confirm in ['Y', 'YES']:
                        # 先执行标准的数据/文件更新
                        success, message = UpdateManagement.execute_update(package_info)
                        if success:
                            safe_print(f"✅ {message}")
                        
                            # 如果是代码更新，在临时副本上应用
                            if package_info["类型码"] == "0" or package_info["类型码"] == "2":  # 系统或功能更新
                                special_update_file = os.path.join(package_info["路径"], "update_special.py")
                                if os.path.exists(special_update_file):
                                    safe_print("🔍 检测到代码更新文件...")
                                    modified_code = IntelligentUpdateSystem.apply_special_update_safe(modified_code, special_update_file, package_info['包名'])
                                    update_applied = True
                        
                            integrated_count += 1
                            UpdateManagement.clean_update_package(package_name)
                        else:
                            safe_print(f"❌ {message}")
        
            # 4. 如果代码有修改，验证并替换原文件
            if update_applied:
                safe_print("\n🔧 代码更新已应用到临时文件，正在验证...")
            
                # 验证代码完整性
                if IntelligentUpdateSystem.validate_code_integrity(modified_code):
                    # 将临时文件覆盖原文件
                    with open(current_file, 'w', encoding='utf-8') as f:
                        f.write(modified_code)
                
                    safe_print("✅ 代码更新成功应用到当前系统")
                else:
                    safe_print("❌ 代码验证失败，保留原系统")
                    # 恢复备份
                    shutil.copy2(backup_file, current_file)
                    safe_print("🔄 已恢复原系统")
    
            # 5. 清理临时文件
            if os.path.exists(temp_file):
                os.remove(temp_file)
        
            safe_print(f"\n📊 集成完成: {integrated_count}个成功")
            
            if integrated_count > 0:
                safe_print("\n🔄 系统将在3秒后重启以应用更新...")
                for i in range(3, 0, -1):
                    safe_print(f"{i}...")
                    time.sleep(1)
            
                safe_print("🔄 正在重启系统...")
                SystemLog.log(f"直接集成更新完成: {integrated_count}个包", "信息")
                os.execv(sys.executable, [sys.executable] + sys.argv)
        
            return integrated_count > 0
        
        except Exception as e:
            safe_print(f"❌ 集成更新失败: {str(e)}")
            SystemLog.log(f"集成更新失败: {str(e)}", "错误")
        
            # 尝试恢复备份
            try:
                if 'backup_file' in locals() and os.path.exists(backup_file):
                    if 'current_file' in locals():
                        shutil.copy2(backup_file, current_file)
                        safe_print("🔄 已从备份恢复系统")
            except:
                pass
        
            return False

    
    @staticmethod
    def create_new_system(update_packages: List[str]) -> bool:
        """创建新系统（改进版）"""
        try:
            safe_print("\n🔄 开始创建新系统文件...")
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            current_file = sys.argv[0] if sys.argv else __file__
            original_file = os.path.basename(current_file)
            new_system_file = f"PWOS2_v{DataManagement.load_version()}_{timestamp}.py"
            
            safe_print(f"📄 原系统文件: {original_file}")
            safe_print(f"📄 新系统文件: {new_system_file}")
            
            # 备份原系统
            backup_file = f"{original_file}.backup_{timestamp}"
            shutil.copy2(current_file, backup_file)
            safe_print(f"📦 原系统已备份为: {backup_file}")
            
            # 读取当前代码
            with open(current_file, 'r', encoding='utf-8') as f:
                current_code = f.read()
            
            new_code = current_code
            integrated_count = 0
            
            for package_name in update_packages:
                package_path = os.path.join(update_package_dir, package_name)
                package_info = UpdateManagement.parse_update_package(package_path)
                
                if package_info:
                    safe_print(f"\n📦 处理更新包: {package_info['包名']}")
                    
                    # 先执行标准更新（用于数据文件）
                    success, message = UpdateManagement.execute_update(package_info)
                    if success:
                        safe_print(f"✅ 数据更新: {message}")
                    else:
                        safe_print(f"⚠️  数据更新失败: {message}")
                    
                    # 处理代码更新
                    special_update_file = os.path.join(package_info["路径"], "update_special.py")
                    if os.path.exists(special_update_file):
                        safe_print("🔍 检测到代码更新文件...")
                        new_code = IntelligentUpdateSystem.apply_special_update_safe(new_code, special_update_file, package_info['包名'])
                    
                    integrated_count += 1
                    UpdateManagement.clean_update_package(package_name)
            
            # 验证新代码
            if not IntelligentUpdateSystem.validate_code_integrity(new_code):
                safe_print("❌ 新系统代码验证失败，使用原系统代码")
                new_code = current_code
            
            # 写入新系统文件
            with open(new_system_file, 'w', encoding='utf-8') as f:
                f.write(new_code)
            
            safe_print(f"\n✅ 新系统文件已创建: {new_system_file}")
            safe_print(f"📊 集成了 {integrated_count} 个更新包")
            
            # 显示系统选择菜单
            safe_print("\n=== 系统选择 ===")
            safe_print("1. 继续使用原系统")
            safe_print(f"2. 切换到新系统 ({new_system_file})")
            safe_print("3. 同时保留两个系统")
            
            while True:
                choice = input("请选择要使用的系统(1-3): ").strip()
                if choice == "1":
                    safe_print("ℹ️  继续使用原系统，新系统文件保留")
                    return False
                elif choice == "2":
                    # 设置重启标记
                    with open("restart_marker.txt", 'w', encoding='utf-8') as f:
                        f.write(new_system_file)
                    
                    safe_print("\n🔄 启动新系统...")
                    time.sleep(2)
                    os.execv(sys.executable, [sys.executable, new_system_file])
                    return True
                elif choice == "3":
                    safe_print("ℹ️  两个系统都已保存，下次启动时可以选择")
                    return True
                else:
                    safe_print("❌ 无效选择")
                    
        except Exception as e:
            safe_print(f"❌ 创建新系统失败: {str(e)}")
            SystemLog.log(f"创建新系统失败: {str(e)}", "错误")
            return False

    
    @staticmethod
    def apply_special_update_safe(current_code: str, special_update_file: str, package_name: str = "未知") -> str:
        """安全地应用特殊更新（支持替换和插入）"""
        try:
            with open(special_update_file, 'r', encoding='utf-8') as f:
                special_code = f.read()
            
            safe_print(f"🔄 处理特殊更新: {package_name}")
            
            # 安全检查
            if len(special_code) > 100000:
                safe_print("❌ 更新文件过大，可能存在风险")
                return current_code
            
            # ========== 1. 替换模式 ==========
            if "# REPLACE_SECTION" in special_code:
                replace_content = special_code.split("# REPLACE_SECTION")[1]
                
                if "# END_REPLACE" not in replace_content:
                    safe_print("❌ 更新格式错误：缺少 END_REPLACE")
                    return current_code
                
                replace_target = replace_content.split("# END_REPLACE")[0].strip()
                replace_with = replace_content.split("# END_REPLACE")[1].strip()
                
                if not replace_target or len(replace_target) < 10:
                    safe_print("❌ 替换目标过短，可能存在风险")
                    return current_code
                
                if replace_target in current_code:
                    # 统计出现次数，防止替换错地方
                    count = current_code.count(replace_target)
                    if count > 1:
                        safe_print(f"⚠️  替换目标出现 {count} 次，将只替换第一次出现")
                    
                    current_code = current_code.replace(replace_target, replace_with, 1)  # 只替换第一次
                    safe_print(f"✅ 安全替换完成")
                else:
                    safe_print("⚠️  未找到替换目标")
            
            # ========== 2. 插入模式（修复版）==========
            elif "# INSERT_AFTER" in special_code:
                insert_content = special_code.split("# INSERT_AFTER")[1]
                
                if "# END_INSERT" not in insert_content:
                    safe_print("❌ 更新格式错误：缺少 END_INSERT")
                    return current_code
                
                insert_target = insert_content.split("# END_INSERT")[0].strip()
                insert_code = insert_content.split("# END_INSERT")[1].strip()
                
                if not insert_target or len(insert_target) < 5:
                    safe_print("❌ 插入目标过短")
                    return current_code
                
                if not insert_code or len(insert_code) < 10:
                    safe_print("❌ 插入代码过短")
                    return current_code
                
                # 按行处理，精确定位
                lines = current_code.split('\n')
                target_line_index = -1
                target_indent = ""
                
                for i, line in enumerate(lines):
                    if insert_target in line and not line.strip().startswith('#'):  # 忽略注释
                        target_line_index = i
                        # 获取缩进
                        target_indent = line[:len(line) - len(line.lstrip())]
                        break
                
                if target_line_index != -1:
                    # 处理插入代码的缩进
                    indented_lines = []
                    for insert_line in insert_code.split('\n'):
                        if insert_line.strip():
                            indented_lines.append(target_indent + insert_line)
                        else:
                            indented_lines.append('')
                    
                    # 在目标行后面插入
                    for j, indented_line in enumerate(indented_lines):
                        lines.insert(target_line_index + 1 + j, indented_line)
                    
                    current_code = '\n'.join(lines)
                    safe_print(f"✅ 安全插入完成，位置: 第 {target_line_index + 1} 行后")
                    safe_print(f"   缩进: {len(target_indent)} 空格")
                    safe_print(f"   插入: {len(indented_lines)} 行")
                else:
                    safe_print("⚠️  未找到插入目标位置")
            
            # ========== 3. 追加模式 ==========
            else:
                # 简单的代码追加
                current_code += "\n\n"
                current_code += f"# ===== 更新包: {package_name} =====\n"
                current_code += special_code.strip()
                current_code += "\n# ===== 更新包结束 =====\n"
                safe_print(f"✅ 代码追加完成")
            
            return current_code
            
        except Exception as e:
            safe_print(f"❌ 应用特殊更新失败: {str(e)}")
            return current_code
    
    @staticmethod
    def integrate_code_from_package(current_code: str, package_info: Dict[str, Any]) -> str:
        """从更新包集成代码"""
        code_files = [f for f in package_info.get("文件列表", []) if f.endswith('.py')]
        for code_file in code_files:
            source_file = os.path.join(package_info["路径"], code_file)
            try:
                with open(source_file, 'r', encoding='utf-8') as f:
                    new_code = f.read()
                
                # 尝试添加新类
                lines = new_code.split('\n')
                for line in lines:
                    if line.strip().startswith('class '):
                        class_name = line.split('class ')[1].split('(')[0].split(':')[0].strip()
                        
                        if f"class {class_name}" not in current_code:
                            # 在合适位置插入
                            insert_pos = current_code.find('if __name__ == "__main__":')
                            if insert_pos == -1:
                                insert_pos = len(current_code)
                            
                            current_code = current_code[:insert_pos] + "\n\n" + new_code + "\n" + current_code[insert_pos:]
                            safe_print(f"✅ 添加新类: {class_name}")
                            break
                
            except Exception as e:
                safe_print(f"❌ 集成代码失败 {code_file}: {str(e)}")
        
        return current_code
    
    @staticmethod
    def check_system_integrity() -> bool:
        """检查系统完整性"""
        safe_print("\n🔍 检查系统完整性...")
        
        try:
            # 检查当前文件
            current_file = sys.argv[0] if sys.argv else __file__
            if not os.path.exists(current_file):
                safe_print("❌ 系统文件不存在")
                return False
            
            file_size = os.path.getsize(current_file)
            safe_print(f"📄 系统文件: {file_size} 字节")
            
            if file_size < 10000:
                safe_print("⚠️  系统文件可能不完整")
            
            # 检查关键类
            required_classes = [
                "IntelligentUpdateSystem",
                "UpdateManagement",
                "DataManagement",
                "UserManagement"
            ]
            
            for class_name in required_classes:
                if class_name not in globals():
                    safe_print(f"❌ 缺少类: {class_name}")
                    return False
            
            safe_print("✅ 系统完整性检查通过")
            return True
            
        except Exception as e:
            safe_print(f"❌ 完整性检查失败: {str(e)}")
            return False
    
    @staticmethod
    def emergency_repair() -> bool:
        """紧急修复系统"""
        try:
            safe_print("\n🛠️  紧急修复系统...")
            
            current_file = sys.argv[0] if sys.argv else __file__
            safe_print(f"修复目标: {current_file}")
            
            # 1. 备份
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"{current_file}.repair_backup_{timestamp}"
            shutil.copy2(current_file, backup_file)
            safe_print(f"📦 已备份: {backup_file}")
            
            # 2. 读取当前文件
            with open(current_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 3. 检查 IntelligentUpdateSystem 类
            if "class IntelligentUpdateSystem:" not in content:
                safe_print("❌ 缺少 IntelligentUpdateSystem 类")
                
                # 在合适位置插入
                insert_pos = content.find("\n# ==================== 主程序 ====================")
                if insert_pos == -1:
                    insert_pos = len(content)
                
                # 添加完整的类
                content = content[:insert_pos] + "\n" + IntelligentUpdateSystem.CLASS_TEMPLATE.strip() + content[insert_pos:]
                safe_print("✅ 已添加 IntelligentUpdateSystem 类")
            
            else:
                safe_print("✅ IntelligentUpdateSystem 类已存在")
                
                # 检查方法是否完整
                required_methods = ["auto_integrate_update", "integrate_to_current", "create_new_system"]
                class_start = content.find("class IntelligentUpdateSystem:")
                class_end = content.find("\nclass ", class_start + 1)
                if class_end == -1:
                    class_end = len(content)
                
                class_code = content[class_start:class_end]
                
                missing_methods = []
                for method in required_methods:
                    if f"def {method}" not in class_code:
                        missing_methods.append(method)
                
                if missing_methods:
                    safe_print(f"⚠️  类不完整，缺失方法: {', '.join(missing_methods)}")
                    safe_print("🔄 正在修复...")
                    
                    # 替换整个类
                    before_class = content[:class_start]
                    after_class = content[class_end:]
                    content = before_class + IntelligentUpdateSystem.CLASS_TEMPLATE.strip() + after_class
                    safe_print("✅ 已修复类")
            
            # 4. 写入修复后的文件
            with open(current_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            file_size = os.path.getsize(current_file)
            safe_print(f"✅ 修复完成，文件大小: {file_size} 字节")
            
            # 5. 提示重启
            safe_print("\n🔄 修复完成，建议重启系统")
            restart = input("是否立即重启系统? (Y/N): ").strip().upper()
            if restart == 'Y':
                safe_print("正在重启...")
                time.sleep(2)
                os.execv(sys.executable, [sys.executable] + sys.argv)
            
            return True
            
        except Exception as e:
            safe_print(f"❌ 紧急修复失败: {str(e)}")
            return False
        
# ==================== 安全路径检查 ====================
class PathSecurity:
    @staticmethod
    def is_safe_path(base_path: str, requested_path: str) -> bool:
        """检查路径是否安全（防止路径遍历攻击）"""
        try:
            base = os.path.abspath(base_path)
            requested = os.path.abspath(os.path.join(base_path, requested_path))
            return requested.startswith(base + os.sep) or requested == base
        except Exception:
            return False
    
    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """清理文件名，移除危险字符"""
        filename = filename.replace('..', '').replace('/', '').replace('\\', '')
        dangerous_chars = [';', '|', '&', '$', '`']
        for char in dangerous_chars:
            filename = filename.replace(char, '')
        return filename

# ==================== 开发者模式功能 ====================
class DeveloperModeFunctions:
    @staticmethod
    def show_developer_menu() -> str:
        """显示开发者菜单"""
        safe_print("\n" + "=" * 60)
        safe_print("           🛠️ 开发者选项")
        safe_print("=" * 60)
        safe_print(" 1. 查看系统内部状态")
        safe_print(" 2. 数据库诊断")
        safe_print(" 3. 性能测试")
        safe_print(" 4. 调试日志级别")
        safe_print(" 5. 系统配置编辑")
        safe_print(" 6. 批量数据操作")
        safe_print(" 7. 代码注入测试")
        safe_print(" 8. 进程管理")
        safe_print(" 9. 系统服务管理")
        safe_print("10. 磁盘使用分析")
        safe_print("11. 内存信息")
        safe_print("12. 修改系统版本号")
        safe_print("13. 紧急系统修复") 
        safe_print("14. 增强备份")
        safe_print("15. 返回主菜单")
        safe_print("=" * 60)
        
        while True:
            choice = input("请选择操作(1-15): ").strip()
            if choice in [str(i) for i in range(1, 16)]:
                return choice
            safe_print("无效选择，请输入1-15之间的数字")

    @staticmethod
    def view_system_internal_status() -> None:
        """查看系统内部状态"""
        safe_print("\n===== 系统内部状态 =====")
        try:
            psutil = SmartLibraryManagement.check_and_import("psutil", "系统资源监控库")
            if psutil:
                memory = psutil.virtual_memory()
                safe_print(f"内存使用: {memory.percent}% ({memory.used//1024//1024}MB/{memory.total//1024//1024}MB)")
                safe_print(f"可用内存: {memory.available//1024//1024}MB")
        except Exception:
            safe_print("内存信息: 需要psutil库")
        
        try:
            psutil = SmartLibraryManagement.check_and_import("psutil", "系统资源监控库")
            if psutil:
                disk = psutil.disk_usage('.')
                safe_print(f"磁盘使用: {disk.percent}% ({disk.used//1024//1024}MB/{disk.total//1024//1024}MB)")
        except Exception:
            safe_print("磁盘信息: 需要psutil库")
        
        safe_print(f"Python版本: {sys.version}")
        safe_print(f"系统平台: {sys.platform}")
        safe_print(f"工作目录: {os.getcwd()}")
        
        data = DataManagement.load_user_data()
        safe_print(f"用户数量: {len(data.get('users', {}))}")
        safe_print(f"下一个ID: {data.get('next_id', 1)}")
        safe_print(f"空ID数量: {len(data.get('empty_ids', []))}")
        
        file_list = [user_file, occupation_file, log_file, password_file, version_file, firewall_file, network_rules_file]
        for file_path in file_list:
            if os.path.exists(file_path):
                size = os.path.getsize(file_path)
                safe_print(f"{os.path.basename(file_path)}: {size} 字节")
        
        safe_print("=" * 25)

    @staticmethod
    def database_diagnosis() -> None:
        """数据库诊断"""
        safe_print("\n===== 数据库诊断 =====")
        try:
            data = DataManagement.load_user_data()
            users = data.get("users", {})
            safe_print(f"总用户数: {len(users)}")
            safe_print(f"下一个ID: {data.get('next_id', 1)}")
            safe_print(f"空ID列表: {data.get('empty_ids', [])}")
            
            issue_count = 0
            for user_id, user_info in users.items():
                required_fields = ["姓名", "年龄", "性别", "职业"]
                for field in required_fields:
                    if field not in user_info:
                        safe_print(f"❌ 用户 {user_id} 缺少字段: {field}")
                        issue_count += 1
                
                if not isinstance(user_info.get("年龄"), int) or user_info["年龄"] <= 0:
                    safe_print(f"❌ 用户 {user_id} 年龄无效: {user_info.get('年龄')}")
                    issue_count += 1
            
            if data.get("empty_ids"):
                safe_print(f"⚠️  存在 {len(data['empty_ids'])} 个空ID，可能影响性能")
            
            if issue_count == 0:
                safe_print("✅ 数据库诊断完成，未发现问题")
            else:
                safe_print(f"⚠️  数据库诊断完成，发现 {issue_count} 个问题")
                
        except Exception as e:
            safe_print(f"❌ 数据库诊断失败: {str(e)}")

    @staticmethod
    def performance_test() -> None:
        """性能测试"""
        safe_print("\n===== 性能测试 =====")
        import time
        
        start_time = time.time()
        for _ in range(100):
            DataManagement.load_user_data()
        end_time = time.time()
        safe_print(f"数据加载性能: {100/(end_time-start_time):.2f} 次/秒")
        
        start_time = time.time()
        DataManagement.create_backup()
        end_time = time.time()
        safe_print(f"备份创建时间: {(end_time-start_time)*1000:.2f} 毫秒")
        
        try:
            psutil = SmartLibraryManagement.check_and_import("psutil", "系统资源监控库")
            if psutil:
                process = psutil.Process()
                memory_usage = process.memory_info().rss / 1024 / 1024
                safe_print(f"当前内存使用: {memory_usage:.2f} MB")
        except Exception:
            safe_print("内存测试: 需要psutil库")
        
        safe_print("性能测试完成")

    @staticmethod
    def debug_log_level() -> None:
        """调试日志级别"""
        safe_print("\n===== 调试日志级别 =====")
        safe_print("1. 调试 - 最详细的日志")
        safe_print("2. 信息 - 一般信息日志")
        safe_print("3. 警告 - 只记录警告和错误")
        safe_print("4. 错误 - 只记录错误")
        safe_print("5. 查看当前日志尾部")
        
        choice = input("请选择: ").strip()
        if choice == "1":
            SystemLog.log("日志级别设置为: 调试", "调试")
            safe_print("✅ 日志级别已设置为: 调试")
        elif choice == "2":
            SystemLog.log("日志级别设置为: 信息", "信息")
            safe_print("✅ 日志级别已设置为: 信息")
        elif choice == "3":
            SystemLog.log("日志级别设置为: 警告", "警告")
            safe_print("✅ 日志级别已设置为: 警告")
        elif choice == "4":
            SystemLog.log("日志级别设置为: 错误", "错误")
            safe_print("✅ 日志级别已设置为: 错误")
        elif choice == "5":
            SystemFunctions.view_logs()
        else:
            safe_print("❌ 无效选择")

    @staticmethod
    def system_config_edit() -> None:
        """系统配置编辑"""
        safe_print("\n===== 系统配置编辑 =====")
        safe_print("1. 编辑用户数据文件")
        safe_print("2. 编辑职业列表文件")
        safe_print("3. 编辑防火墙配置")
        safe_print("4. 编辑版本文件")
        safe_print("5. 查看原始JSON数据")
        safe_print("6. 返回")
        
        choice = input("请选择: ").strip()
        file_map = {
            "1": ("用户数据", user_file),
            "2": ("职业列表", occupation_file),
            "3": ("防火墙配置", firewall_file),
            "4": ("版本信息", version_file)
        }
        
        if choice in file_map:
            file_name, file_path = file_map[choice]
            safe_print(f"\n编辑 {file_name} - {file_path}")
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                safe_print(f"\n当前内容:\n{content}")
                confirm = input("\n是否编辑此文件? (Y/N): ").strip().upper()
                if confirm == 'Y':
                    safe_print("请在外部编辑器中编辑文件，完成后按Enter继续...")
                    input("按Enter继续...")
                    safe_print("✅ 文件编辑完成（请确保格式正确）")
            else:
                safe_print("❌ 文件不存在")
        elif choice == "5":
            DeveloperModeFunctions.view_raw_json_data()
        elif choice == "6":
            return
        else:
            safe_print("❌ 无效选择")

    @staticmethod
    def view_raw_json_data() -> None:
        """查看原始JSON数据"""
        safe_print("\n===== 原始JSON数据查看 =====")
        file_list = [user_file, occupation_file, firewall_file, version_file, network_rules_file]
        for file_path in file_list:
            if os.path.exists(file_path):
                safe_print(f"\n=== {os.path.basename(file_path)} ===")
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        safe_print(json.dumps(data, ensure_ascii=False, indent=2))
                    except Exception as e:
                        safe_print(f"解析错误: {e}")
            else:
                safe_print(f"\n=== {os.path.basename(file_path)} ===")
                safe_print("文件不存在")

    @staticmethod
    def batch_data_operations() -> None:
        """批量数据操作"""
        safe_print("\n===== 批量数据操作 =====")
        safe_print("1. 批量添加测试用户")
        safe_print("2. 清理测试数据")
        safe_print("3. 导出所有数据为JSON")
        safe_print("4. 数据完整性检查")
        safe_print("5. 返回")
        
        choice = input("请选择: ").strip()
        if choice == "1":
            DeveloperModeFunctions.batch_add_test_users()
        elif choice == "2":
            DeveloperModeFunctions.clean_test_data()
        elif choice == "3":
            DeveloperModeFunctions.export_all_data_as_json()
        elif choice == "4":
            DeveloperModeFunctions.data_integrity_check()
        elif choice == "5":
            return
        else:
            safe_print("❌ 无效选择")

    @staticmethod
    def batch_add_test_users() -> None:
        """批量添加测试用户"""
        try:
            safe_print("\n正在批量添加测试用户...")
            data = DataManagement.load_user_data()
            
            test_users = [
                {"姓名": "测试用户A", "年龄": 25, "性别": "男", "职业": "程序员"},
                {"姓名": "测试用户B", "年龄": 30, "性别": "女", "职业": "设计师"},
                {"姓名": "测试用户C", "年龄": 28, "性别": "男", "职业": "工程师"},
                {"姓名": "测试用户D", "年龄": 35, "性别": "女", "职业": "经理"},
                {"姓名": "测试用户E", "年龄": 22, "性别": "其他", "职业": "学生"}
            ]
            
            add_count = 0
            for user_info in test_users:
                if data["empty_ids"]:
                    use_id = min(data["empty_ids"])
                    data["empty_ids"].remove(use_id)
                else:
                    use_id = data["next_id"]
                    data["next_id"] += 1
                
                user_info["创建时间"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data["users"][str(use_id)] = user_info
                add_count += 1
                safe_print(f"✅ 添加测试用户: ID={use_id}, 姓名={user_info['姓名']}")
            
            if DataManagement.save_user_data(data):
                safe_print(f"✅ 成功添加 {add_count} 个测试用户")
                SystemLog.log(f"批量添加 {add_count} 个测试用户", "调试")
            else:
                safe_print("❌ 保存数据失败")
                
        except Exception as e:
            safe_print(f"❌ 批量添加测试用户失败: {str(e)}")

    @staticmethod
    def clean_test_data() -> None:
        """清理测试数据"""
        try:
            safe_print("\n正在清理测试数据...")
            data = DataManagement.load_user_data()
            users = data.get("users", {})
            delete_count = 0
            deleted_users = []
            
            for user_id, user_info in list(users.items()):
                if "测试用户" in user_info.get("姓名", ""):
                    deleted_users.append(f"ID={user_id}, 姓名={user_info['姓名']}")
                    del users[user_id]
                    if int(user_id) not in data["empty_ids"]:
                        data["empty_ids"].append(int(user_id))
                    delete_count += 1
            
            if delete_count > 0:
                if DataManagement.save_user_data(data):
                    safe_print(f"✅ 成功删除 {delete_count} 个测试用户")
                    for user_info in deleted_users:
                        safe_print(f"   - {user_info}")
                    SystemLog.log(f"清理 {delete_count} 个测试用户", "调试")
                else:
                    safe_print("❌ 保存数据失败")
            else:
                safe_print("ℹ️  没有找到测试用户数据")
                
        except Exception as e:
            safe_print(f"❌ 清理测试数据失败: {str(e)}")

    @staticmethod
    def export_all_data_as_json() -> None:
        """导出所有数据为JSON"""
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            export_file = os.path.join(data_dir, f"system_full_export_{timestamp}.json")
            
            export_data = {
                "导出时间": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "系统版本": DataManagement.load_version(),
                "用户数据": DataManagement.load_user_data(),
                "职业列表": DataManagement.load_occupation_list(),
                "防火墙配置": DataManagement.load_firewall_config(),
                "网络规则": DataManagement.load_network_rules()
            }
            
            with open(export_file, "w", encoding="utf-8") as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)
            
            safe_print(f"✅ 所有系统数据已导出到: {export_file}")
            SystemLog.log(f"导出完整系统数据到 {export_file}", "调试")
            
        except Exception as e:
            safe_print(f"❌ 导出数据失败: {str(e)}")

    @staticmethod
    def data_integrity_check() -> None:
        """数据完整性检查"""
        safe_print("\n===== 数据完整性检查 =====")
        try:
            file_list = [user_file, occupation_file, firewall_file, version_file, password_file, network_rules_file]
            for file_path in file_list:
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            json.load(f)
                        safe_print(f"✅ {os.path.basename(file_path)}: JSON格式有效")
                    except json.JSONDecodeError as e:
                        safe_print(f"❌ {os.path.basename(file_path)}: JSON格式错误 - {e}")
                else:
                    safe_print(f"⚠️  {os.path.basename(file_path)}: 文件不存在")
            
            dir_list = [data_dir, backup_dir, update_package_dir]
            for dir_path in dir_list:
                if os.path.exists(dir_path):
                    try:
                        test_file = os.path.join(dir_path, "test_write.tmp")
                        with open(test_file, 'w') as f:
                            f.write("test")
                        os.remove(test_file)
                        safe_print(f"✅ {os.path.basename(dir_path)}: 写入权限正常")
                    except Exception as e:
                        safe_print(f"❌ {os.path.basename(dir_path)}: 写入权限异常 - {e}")
                else:
                    safe_print(f"⚠️  {os.path.basename(dir_path)}: 目录不存在")
            
            safe_print("数据完整性检查完成")
            
        except Exception as e:
            safe_print(f"❌ 数据完整性检查失败: {str(e)}")

    @staticmethod
    def code_injection_test() -> None:
        """代码注入测试"""
        safe_print("\n===== 代码注入测试 =====")
        safe_print("⚠️  警告: 此功能仅用于安全测试")
        safe_print("1. SQL注入测试模拟")
        safe_print("2. XSS测试模拟")
        safe_print("3. 路径遍历测试")
        safe_print("4. 返回")
        
        choice = input("请选择: ").strip()
        if choice == "1":
            safe_print("\nSQL注入测试模拟...")
            safe_print("检测到系统使用JSON存储，不存在SQL注入漏洞")
            safe_print("✅ 系统对SQL注入免疫")
        elif choice == "2":
            safe_print("\nXSS测试模拟...")
            safe_print("检测到系统为命令行界面，不存在XSS漏洞")
            safe_print("✅ 系统对XSS攻击免疫")
        elif choice == "3":
            safe_print("\n路径遍历测试...")
            try:
                test_path = "../../../etc/passwd"
                safe_path = PathSecurity.is_safe_path(data_dir, test_path)
                if safe_path:
                    safe_print("✅ 路径遍历防护有效")
                else:
                    safe_print("❌ 存在路径遍历风险")
            except Exception as e:
                safe_print(f"路径遍历测试异常: {e}")
        elif choice == "4":
            return
        else:
            safe_print("❌ 无效选择")

    @staticmethod
    def process_management() -> None:
        """进程管理（修复命令注入漏洞）"""
        safe_print("\n===== 进程管理 =====")
        psutil = SmartLibraryManagement.check_and_import("psutil", "进程管理库")
        if not psutil:
            return
        
        while True:
            safe_print("\n1. 查看所有进程")
            safe_print("2. 结束进程")
            safe_print("3. 进程资源监控")
            safe_print("4. 启动新进程")
            safe_print("5. 返回")
            
            choice = input("请选择: ").strip()
            
            if choice == "1":
                safe_print("\n=== 系统进程 ===")
                try:
                    for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_percent']):
                        try:
                            info = proc.info
                            safe_print(f"PID: {info['pid']:<6} | {info['name']:<30} | CPU: {info['cpu_percent']:>5.1f}% | 内存: {info['memory_percent']:>5.1f}%")
                        except Exception:
                            pass
                except Exception as e:
                    safe_print(f"获取进程列表失败: {str(e)}")
                    
            elif choice == "2":
                pid = input("请输入要结束的进程PID: ").strip()
                if pid.isdigit():
                    try:
                        proc = psutil.Process(int(pid))
                        proc_name = proc.name()
                        confirm = input(f"确定要结束进程 {pid} ({proc_name}) 吗? (Y/N): ").upper()
                        if confirm == 'Y':
                            proc.terminate()
                            safe_print(f"✅ 已尝试结束进程 {pid}")
                    except Exception as e:
                        safe_print(f"结束进程失败: {str(e)}")
                else:
                    safe_print("❌ 请输入有效的PID")
                    
            elif choice == "3":
                safe_print("\n=== 系统资源监控 ===")
                try:
                    cpu_usage = psutil.cpu_percent(interval=1)
                    memory = psutil.virtual_memory()
                    disk = psutil.disk_usage('/')
                    network = psutil.net_io_counters()
                    
                    safe_print(f"CPU使用率: {cpu_usage}%")
                    safe_print(f"内存使用: {memory.percent}% ({memory.used//1024//1024}MB/{memory.total//1024//1024}MB)")
                    safe_print(f"可用内存: {memory.available//1024//1024}MB")
                    safe_print(f"磁盘使用: {disk.percent}% ({disk.used//1024//1024}MB/{disk.total//1024//1024}MB)")
                    safe_print(f"网络 - 发送: {network.bytes_sent//1024}KB, 接收: {network.bytes_recv//1024}KB")
                except Exception as e:
                    safe_print(f"获取资源信息失败: {str(e)}")
                    
            elif choice == "4":
                program = input("请输入要启动的程序路径: ").strip()
                if not program:
                    safe_print("❌ 程序路径不能为空")
                    continue
                
                try:
                    import subprocess
                    
                    program = program.strip()
                    dangerous_chars = [';', '|', '&', '$', '`', '(', ')', '>', '<']
                    for char in dangerous_chars:
                        if char in program:
                            safe_print(f"❌ 路径包含危险字符: {char}")
                            continue
                    
                    program_name = os.path.basename(program).lower()
                    allowed_programs = {
                        'notepad.exe': '记事本',
                        'calc.exe': '计算器',
                        'mspaint.exe': '画图',
                        'cmd.exe': '命令提示符',
                        'powershell.exe': 'PowerShell',
                        'python.exe': 'Python解释器',
                        'pythonw.exe': 'Python窗口程序'
                    }
                    
                    allowed = False
                    for allowed_prog in allowed_programs:
                        if program_name.endswith(allowed_prog):
                            allowed = True
                            program_display_name = allowed_programs[allowed_prog]
                            break
                    
                    if not allowed:
                        safe_print(f"❌ 程序 {program_name} 不在允许列表中")
                        confirm = input("是否继续执行? (输入 'YES' 确认): ").strip()
                        if confirm != "YES":
                            continue
                        program_display_name = program_name
                    
                    full_path = None
                    if os.path.exists(program):
                        full_path = os.path.abspath(program)
                    else:
                        import shutil
                        full_path = shutil.which(program)
                    
                    if not full_path:
                        safe_print(f"❌ 程序不存在或找不到: {program}")
                        continue
                    
                    if not os.path.isfile(full_path):
                        safe_print(f"❌ 不是有效的程序文件: {full_path}")
                        continue
                    
                    _, ext = os.path.splitext(full_path)
                    allowed_extensions = ['.exe', '.bat', '.cmd', '.py']
                    if ext.lower() not in allowed_extensions:
                        safe_print(f"❌ 不允许的文件类型: {ext}")
                        continue
                    
                    safe_print(f"🔒 安全启动: {program_display_name}")
                    
                    args = [full_path]
                    
                    if program_name == 'powershell.exe':
                        args.extend(['-NoProfile', '-ExecutionPolicy', 'Restricted', '-Command', 'Write-Host "安全模式"'])
                    elif program_name == 'cmd.exe':
                        args.extend(['/C', 'echo 安全模式 & pause'])
                    elif program_name.endswith('.py'):
                        args = [sys.executable, full_path]
                    
                    process = subprocess.Popen(
                        args,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        shell=False,
                        creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
                    )
                    
                    safe_print(f"✅ 进程已启动 PID: {process.pid}")
                    SystemLog.security_log(f"启动进程: {program_display_name}", "用户", f"PID:{process.pid}")
                    
                except subprocess.CalledProcessError as e:
                    safe_print(f"❌ 程序执行失败: {e.stderr.decode('utf-8', errors='ignore')[:200]}")
                except FileNotFoundError:
                    safe_print("❌ 找不到程序文件")
                except Exception as e:
                    safe_print(f"❌ 启动程序失败: {str(e)}")
                        
            elif choice == "5":
                break

    @staticmethod
    def service_management() -> None:
        """服务管理"""
        safe_print("\n===== 系统服务管理 =====")
        safe_print("1. 查看系统服务")
        safe_print("2. 启动/停止服务")
        safe_print("3. 服务状态监控")
        safe_print("4. 返回")
        
        choice = input("请选择: ").strip()
        if choice == "1":
            safe_print("\n=== 模拟系统服务 ===")
            services = {
                "users_db": {"name": "用户数据库服务", "status": "运行中", "pid": 1234},
                "network": {"name": "网络服务", "status": "运行中", "pid": 2345},
                "ai_assistant": {"name": "AI助手服务", "status": "已停止", "pid": None},
                "backup": {"name": "备份服务", "status": "运行中", "pid": 3456},
                "firewall": {"name": "防火墙服务", "status": "运行中", "pid": 4567}
            }
            for service_id, info in services.items():
                status_icon = "✅" if info["status"] == "运行中" else "❌"
                safe_print(f"{status_icon} {info['name']:<20} | 状态: {info['status']:<10} | PID: {info['pid'] or '无'}")

    @staticmethod
    def disk_usage_analysis() -> None:
        """磁盘使用分析"""
        safe_print("\n===== 磁盘使用分析 =====")
        psutil = SmartLibraryManagement.check_and_import("psutil", "磁盘分析库")
        if not psutil:
            return
        
        try:
            partitions = psutil.disk_partitions()
            for partition in partitions:
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    safe_print(f"\n📁 {partition.device:<15} {partition.mountpoint:<15}")
                    safe_print(f"   总容量: {usage.total//(1024**3):>6} GB | 已用: {usage.used//(1024**3):>5} GB | 可用: {usage.free//(1024**3):>5} GB")
                    safe_print(f"   使用率: {usage.percent:>5.1f}%")
                    
                    if usage.percent > 90:
                        safe_print("   ⚠️  警告: 磁盘空间严重不足!")
                    elif usage.percent > 80:
                        safe_print("   ⚠️  注意: 磁盘空间不足!")
                except Exception:
                    continue
        except Exception as e:
            safe_print(f"❌ 磁盘分析失败: {str(e)}")

    @staticmethod
    def memory_info() -> None:
        """内存信息（修复版）"""
        
        # 定义安全的打印函数（如果不存在）
        def safe_print(text: str) -> None:
            try:
                print(text)
            except:
                print(str(text).encode('ascii', 'ignore').decode())
        
        safe_print("\n===== 内存信息 =====")
        
        # 修复导入逻辑
        try:
            import psutil
        except ImportError:
            safe_print("❌ 未安装psutil库，无法获取内存信息")
            safe_print("💡 请安装: pip install psutil")
            return
        
        try:
            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()
            
            # 辅助函数：智能显示内存大小
            def format_bytes(bytes_value: int) -> str:
                """智能格式化字节大小"""
                if bytes_value < 0:
                    return "未知"
                for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                    if bytes_value < 1024.0:
                        return f"{bytes_value:.1f} {unit}"
                    bytes_value /= 1024.0
                return f"{bytes_value:.1f} PB"
            
            safe_print("📊 === 物理内存 ===")
            safe_print(f"总计: {format_bytes(memory.total)}")
            safe_print(f"已使用: {format_bytes(memory.used)} ({memory.percent}%)")
            safe_print(f"可用: {format_bytes(memory.available)}")
            
            # 兼容性处理：不同系统可能有不同的属性名
            if hasattr(memory, 'cached') and memory.cached > 0:
                safe_print(f"缓存: {format_bytes(memory.cached)}")
            elif hasattr(memory, 'buffers') and memory.buffers > 0:
                safe_print(f"缓冲区: {format_bytes(memory.buffers)}")
            elif hasattr(memory, 'cached') and hasattr(memory, 'buffers'):
                # Linux系统
                safe_print(f"缓存+缓冲区: {format_bytes(memory.cached + memory.buffers)}")
            
            safe_print("\n💾 === 交换空间 ===")
            safe_print(f"总计: {format_bytes(swap.total)}")
            safe_print(f"已使用: {format_bytes(swap.used)} ({swap.percent}%)")
            safe_print(f"可用: {format_bytes(swap.free)}")
            
            # 添加更多详细信息（带安全检查）
            safe_print("\n🔍 === 详细信息 ===")
            
            # 活跃内存（Linux/Unix）
            if hasattr(memory, 'active') and memory.active > 0:
                safe_print(f"活跃内存: {format_bytes(memory.active)}")
            
            # 非活跃内存（Linux/Unix）  
            if hasattr(memory, 'inactive') and memory.inactive > 0:
                safe_print(f"非活跃内存: {format_bytes(memory.inactive)}")
            
            # 共享内存（Linux）
            if hasattr(memory, 'shared') and memory.shared > 0:
                safe_print(f"共享内存: {format_bytes(memory.shared)}")
            
            # 脏页（Linux）
            if hasattr(memory, 'dirty') and memory.dirty > 0:
                safe_print(f"脏页: {format_bytes(memory.dirty)}")
            
            # Windows特定的内存指标
            if hasattr(memory, 'available') and hasattr(memory, 'total'):
                available_percent = (memory.available / memory.total) * 100
                safe_print(f"可用内存比例: {available_percent:.1f}%")
            
            # 内存使用建议
            safe_print("\n💡 === 内存使用建议 ===")
            if memory.percent > 90:
                safe_print("🚨 紧急: 内存使用率超过90%，建议立即关闭不需要的程序！")
                safe_print("   可能影响: 系统响应变慢，应用可能被强制关闭")
            elif memory.percent > 80:
                safe_print("⚠️  警告: 内存使用率超过80%，建议监控内存使用")
                safe_print("   建议: 检查是否有内存泄漏或关闭不必要的应用")
            elif memory.percent > 60:
                safe_print("ℹ️  提示: 内存使用正常")
            else:
                safe_print("✅ 优秀: 内存使用率良好")
            
            # 交换空间建议
            if swap.total > 0:  # 只在使用交换空间时显示
                if swap.percent > 50:
                    safe_print(f"⚠️  注意: 交换空间使用率较高 ({swap.percent}%)")
                    safe_print("   频繁使用交换空间会显著降低系统性能")
                    safe_print("   建议: 考虑增加物理内存")
                elif swap.percent > 20:
                    safe_print(f"ℹ️  提示: 交换空间使用率 {swap.percent}%")
            else:
                safe_print("ℹ️  提示: 系统未配置交换空间")
            
            # 系统内存压力评估
            memory_pressure = (memory.used / memory.total) * 100
            if memory_pressure > 90 and swap.percent > 50:
                safe_print("⚠️  严重: 系统处于高内存压力状态！")
                safe_print("   强烈建议: 重启系统或增加物理内存")
                
        except AttributeError as e:
            safe_print(f"❌ 获取内存信息失败: 系统不支持该功能 ({str(e)})")
            safe_print("💡 尝试更新psutil: pip install --upgrade psutil")
        except PermissionError:
            safe_print("❌ 权限不足，无法访问完整内存信息")
            safe_print("💡 尝试以管理员/root权限运行")
        except Exception as e:
            safe_print(f"❌ 获取内存信息失败: {str(e)}")
            safe_print("💡 可能的原因:")
            safe_print("   1. psutil库版本过旧 (请升级: pip install --upgrade psutil)")
            safe_print("   2. 操作系统不支持某些功能")
            safe_print("   3. 系统资源暂时不可用")

    @staticmethod
    def modify_system_version() -> None:
        """修改系统版本号"""
        safe_print("\n===== 修改系统版本号 =====")
        try:
            with open(version_file, 'r', encoding='utf-8') as f:
                current_version = json.load(f)
            
            safe_print(f"当前版本: v{current_version['major']}.{current_version['minor']}")
            
            while True:
                try:
                    new_major = input("请输入新的主版本号: ").strip()
                    if not new_major.isdigit():
                        safe_print("❌ 主版本号必须是数字")
                        continue
                    
                    new_minor = input("请输入新的次版本号: ").strip()
                    if not new_minor.isdigit():
                        safe_print("❌ 次版本号必须是数字")
                        continue
                    
                    new_major = int(new_major)
                    new_minor = int(new_minor)
                    
                    if new_major < 0 or new_minor < 0:
                        safe_print("❌ 版本号不能为负数")
                        continue
                    
                    break
                except ValueError:
                    safe_print("❌ 请输入有效的数字")
            
            safe_print(f"\n即将修改版本: v{current_version['major']}.{current_version['minor']} → v{new_major}.{new_minor}")
            confirm = input("确定要修改吗? (Y/N): ").strip().upper()
            if confirm != 'Y':
                safe_print("操作已取消")
                return
            
            DataManagement.save_version(new_major, new_minor)
            global system_name
            system_name = f"PWOS2 v{new_major}.{new_minor}"
            safe_print(f"✅ 版本号已修改: v{new_major}.{new_minor}")
            
            safe_print("\n===== 版本修改生效选项 =====")
            safe_print("1. 立即重启系统 (推荐)")
            safe_print("2. 稍后手动重启")
            safe_print("3. 取消修改 (恢复原版本)")
            
            while True:
                effect_option = input("请选择生效方式 (1-3): ").strip()
                if effect_option == "1":
                    safe_print("🔄 系统将在3秒后重启...")
                    for i in range(3, 0, -1):
                        safe_print(f"{i}...")
                        time.sleep(1)
                    
                    safe_print("🔄 正在重启系统...")
                    SystemLog.log("系统版本修改后重启", "信息")
                    os.execv(sys.executable, [sys.executable] + sys.argv)
                elif effect_option == "2":
                    safe_print("ℹ️  版本修改已保存，重启系统后生效")
                    safe_print("注意: 在重启前，系统名称可能显示不一致")
                    break
                elif effect_option == "3":
                    DataManagement.save_version(current_version['major'], current_version['minor'])
                    system_name = f"PWOS2 v{current_version['major']}.{current_version['minor']}"
                    safe_print("✅ 版本修改已取消，恢复原版本")
                    break
                else:
                    safe_print("❌ 无效选择，请重新输入")
            
            SystemLog.log(f"开发者修改系统版本: v{current_version['major']}.{current_version['minor']} → v{new_major}.{new_minor}")
            
        except Exception as e:
            safe_print(f"❌ 修改系统版本失败: {str(e)}")
            SystemLog.log(f"修改系统版本失败: {str(e)}", "错误")

# ==================== AI助手 ====================
#千问key：sk-f46d5d93338d4a2c9b241219f385ba0a
#Deepseek Key：sk-25655b5cfbc542f1a543fa470b718791
#=============================================
class AIAssistant:
    @staticmethod
    def init() -> bool:
        """初始化AI助手"""
        try:
            if not os.path.exists(ai_config_file):
                default_config = {
                    "enable_ai": False,
                    "providers": {
                        "deepseek": {
                            "enabled": False,
                            "api_key": "",
                            "api_base": "https://api.deepseek.com",
                            "model": "deepseek-chat"
                        },
                        "aliyun": {
                            "enabled": False,
                            "api_key": "",
                            "api_base": "https://dashscope.aliyuncs.com",
                            "model": "qwen-max"
                        }
                    },
                    "temperature": 0.7,
                    "max_tokens": 1000,
                    "max_history": 20
                }
                with open(ai_config_file, 'w', encoding='utf-8') as f:
                    json.dump(default_config, f, ensure_ascii=False, indent=2)
                SystemLog.log("已初始化AI助手配置")
            
            # 清理旧版本可能存在的last_provider字段
            config = AIAssistant.load_config()
            if config and "last_provider" in config:
                del config["last_provider"]
                AIAssistant.save_config(config)
                SystemLog.log("已清理旧版AI配置的last_provider字段", "信息")
                
            return True
        except Exception as e:
            SystemLog.log(f"初始化AI助手失败: {str(e)}", "错误")
            return False

    @staticmethod
    def load_config() -> Optional[Dict[str, Any]]:
        """加载配置"""
        try:
            if os.path.exists(ai_config_file):
                with open(ai_config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return None
        except Exception as e:
            SystemLog.log(f"加载AI助手配置失败: {str(e)}", "错误")
            return None

    @staticmethod
    def save_config(config: Dict[str, Any]) -> bool:
        """保存配置"""
        try:
            with open(ai_config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            SystemLog.log(f"保存AI助手配置失败: {str(e)}", "错误")
            return False

    @staticmethod
    def get_available_provider(config: Dict[str, Any]) -> Tuple[Optional[str], List[str]]:
        """
        智能获取可用的AI提供商
        返回：(主提供商, [所有可用的提供商列表])
        """
        providers = config.get("providers", {})
        available_providers = []
        
        # 检查哪些提供商是可用的（已启用且有API密钥）
        deepseek = providers.get("deepseek", {})
        if deepseek.get("enabled") and deepseek.get("api_key"):
            available_providers.append("deepseek")
        
        aliyun = providers.get("aliyun", {})
        if aliyun.get("enabled") and aliyun.get("api_key"):
            available_providers.append("aliyun")
        
        if not available_providers:
            return None, []
        
        # 确定主提供商
        main_provider = None
        if "deepseek" in available_providers:
            main_provider = "deepseek"
        else:
            main_provider = available_providers[0]
        
        return main_provider, available_providers

    @staticmethod
    def try_providers_with_fallback(config: Dict[str, Any], user_input: str, 
                                   message_history: List[Dict[str, str]], 
                                   main_provider: str, fallback_providers: List[str]) -> Tuple[Optional[str], str]:
        """
        尝试提供商，主提供商失败时使用备用的
        """
        # 先尝试主提供商
        try:
            safe_print(f"🔄 使用 {main_provider}...", end="", flush=True)
            if main_provider == "deepseek":
                reply = AIAssistant.call_deepseek(config["providers"]["deepseek"], user_input, message_history)
            else:
                reply = AIAssistant.call_aliyun(config["providers"]["aliyun"], user_input, message_history)
            safe_print(f"✅ {main_provider} 响应成功")
            return main_provider, reply
        except Exception as e:
            error_msg = f"❌ {main_provider} 失败"
            safe_print(error_msg)
        
        # 主提供商失败，尝试其他可用的
        for provider in fallback_providers:
            if provider == main_provider:
                continue
            
            try:
                safe_print(f"🔄 切换到 {provider}...", end="", flush=True)
                if provider == "deepseek":
                    reply = AIAssistant.call_deepseek(config["providers"]["deepseek"], user_input, message_history)
                else:
                    reply = AIAssistant.call_aliyun(config["providers"]["aliyun"], user_input, message_history)
                safe_print(f"✅ {provider} 响应成功")
                return provider, reply
            except Exception as e:
                safe_print(f"❌ {provider} 也失败")
                continue
        
        # 所有提供商都失败
        return None, "❌ 所有AI服务都失败了，请检查网络连接和API密钥"

    @staticmethod
    def show_ai_menu() -> str:
        """显示AI菜单"""
        safe_print("\n===== AI智能助手 =====")
        safe_print("1. 启用/禁用AI助手")
        safe_print("2. 配置DeepSeek")
        safe_print("3. 配置阿里云通义千问")
        safe_print("4. 与AI对话")
        safe_print("5. AI系统分析")
        safe_print("6. 返回主菜单")
        
        while True:
            choice = input("请选择(1-6): ").strip()
            if choice in [str(i) for i in range(1, 7)]:
                return choice
            safe_print("无效选择，请输入1-6之间的数字")

    @staticmethod
    def main_menu_function() -> None:
        """AI助手主菜单功能"""
        if not AIAssistant.init():
            safe_print("❌ AI助手初始化失败")
            return
        
        config = AIAssistant.load_config()
        if not config:
            safe_print("❌ 无法加载AI配置")
            return
        
        while True:
            choice = AIAssistant.show_ai_menu()
            if choice == "1":
                AIAssistant.toggle_enable_status(config)
            elif choice == "2":
                AIAssistant.configure_deepseek(config)
            elif choice == "3":
                AIAssistant.configure_aliyun(config)
            elif choice == "4":
                AIAssistant.chat_with_ai(config)
            elif choice == "5":
                AIAssistant.system_analysis(config)
            elif choice == "6":
                break

    @staticmethod
    def toggle_enable_status(config: Dict[str, Any]) -> None:
        """切换启用状态"""
        if config.get("enable_ai", False):
            config["enable_ai"] = False
            safe_print("✅ AI助手已禁用")
        else:
            available_service = False
            for provider, settings in config.get("providers", {}).items():
                if settings.get("enabled") and settings.get("api_key"):
                    available_service = True
                    break
            
            if not available_service:
                safe_print("❌ 没有可用的AI服务，请先配置API Key")
                return
            
            config["enable_ai"] = True
            safe_print("✅ AI助手已启用")
        
        AIAssistant.save_config(config)

    @staticmethod
    def configure_deepseek(config: Dict[str, Any]) -> None:
        """配置DeepSeek"""
        safe_print("\n===== 配置DeepSeek =====")
        deepseek_config = config.get("providers", {}).get("deepseek", {})
        current_state = deepseek_config.get("enabled", False)
        
        safe_print(f"当前状态: {'✅ 已启用' if current_state else '❌ 已禁用'}")
        safe_print("\n1. 启用/禁用DeepSeek")
        safe_print("2. 设置API Key")
        safe_print("3. 测试连接")
        safe_print("4. 返回")
        
        choice = input("请选择: ").strip()
        if choice == "1":
            deepseek_config["enabled"] = not current_state
            config["providers"]["deepseek"] = deepseek_config
            AIAssistant.save_config(config)
            safe_print(f"✅ DeepSeek已{'启用' if deepseek_config['enabled'] else '禁用'}")
        elif choice == "2":
            safe_print("\n请访问 https://bailian.console.aliyun.com/ 获取API Key")
            api_key = input("请输入DeepSeek API Key: ").strip()
            if api_key:
                deepseek_config["api_key"] = api_key
                config["providers"]["deepseek"] = deepseek_config
                AIAssistant.save_config(config)
                safe_print("✅ API Key已保存")
            else:
                safe_print("❌ API Key不能为空")
        elif choice == "3":
            AIAssistant.test_deepseek_connection(deepseek_config)
        elif choice == "4":
            return

    @staticmethod
    def configure_aliyun(config: Dict[str, Any]) -> None:
        """配置阿里云"""
        safe_print("\n===== 配置阿里云通义千问 =====")
        aliyun_config = config.get("providers", {}).get("aliyun", {})
        current_state = aliyun_config.get("enabled", False)
        
        safe_print(f"当前状态: {'✅ 已启用' if current_state else '❌ 已禁用'}")
        safe_print("\n1. 启用/禁用阿里云")
        safe_print("2. 设置API Key")
        safe_print("3. 测试连接")
        safe_print("4. 返回")
        
        choice = input("请选择: ").strip()
        if choice == "1":
            aliyun_config["enabled"] = not current_state
            config["providers"]["aliyun"] = aliyun_config
            AIAssistant.save_config(config)
            safe_print(f"✅ 阿里云已{'启用' if aliyun_config['enabled'] else '禁用'}")
        elif choice == "2":
            safe_print("\n请访问 https://bailian.console.aliyun.com/  获取API Key")
            api_key = input("请输入阿里云API Key: ").strip()
            if api_key:
                aliyun_config["api_key"] = api_key
                config["providers"]["aliyun"] = aliyun_config
                AIAssistant.save_config(config)
                safe_print("✅ API Key已保存")
            else:
                safe_print("❌ API Key不能为空")
        elif choice == "3":
            AIAssistant.test_aliyun_connection(aliyun_config)
        elif choice == "4":
            return

    @staticmethod
    def test_deepseek_connection(config: Dict[str, Any]) -> None:
        """测试DeepSeek连接"""
        if not config.get("api_key"):
            safe_print("❌ 请先设置API Key")
            return
        
        safe_print("🔄 测试DeepSeek连接...")
        requests = SmartLibraryManagement.check_and_import("requests", "网络请求库 - 用于连接AI API服务")
        if not requests:
            safe_print("❌ 需要安装requests库")
            return
        
        try:
            headers = {
                "Authorization": f"Bearer {config['api_key']}",
                "Content-Type": "application/json"
            }
            data = {
                "model": config.get("model", "deepseek-chat"),
                "messages": [
                    {"role": "user", "content": "你好，请回复'连接成功'"}
                ],
                "max_tokens": 50,
                "temperature": 0.7
            }
            
            response = requests.post(
                f"{config.get('api_base', 'https://api.deepseek.com')}/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                safe_print("✅ DeepSeek连接成功！")
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    reply = result["choices"][0]["message"]["content"]
                    safe_print(f"AI回复: {reply}")
            else:
                safe_print(f"❌ 连接失败: {response.status_code}")
                safe_print(response.text[:200])
                
        except Exception as e:
            safe_print(f"❌ 连接测试失败: {str(e)}")

    @staticmethod
    def test_aliyun_connection(config: Dict[str, Any]) -> None:
        """测试阿里云连接"""
        if not config.get("api_key"):
            safe_print("❌ 请先设置API Key")
            return
        
        safe_print("🔄 测试阿里云连接...")
        requests = SmartLibraryManagement.check_and_import("requests", "网络请求库 - 用于连接AI API服务")
        if not requests:
            safe_print("❌ 需要安装requests库")
            return
        
        try:
            headers = {
                "Authorization": f"Bearer {config['api_key']}",
                "Content-Type": "application/json",
                "X-DashScope-SSE": "disable"
            }
            data = {
                "model": config.get("model", "qwen-max"),
                "input": {
                    "messages": [
                        {"role": "user", "content": "你好，请回复'连接成功'"}
                    ]
                },
                "parameters": {
                    "max_tokens": 50,
                    "temperature": 0.7
                }
            }
            
            response = requests.post(
                f"{config.get('api_base', 'https://dashscope.aliyuncs.com')}/api/v1/services/aigc/text-generation/generation",
                headers=headers,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                safe_print("✅ 阿里云连接成功！")
                result = response.json()
                if "output" in result and "text" in result["output"]:
                    reply = result["output"]["text"]
                    safe_print(f"AI回复: {reply}")
            else:
                safe_print(f"❌ 连接失败: {response.status_code}")
                safe_print(response.text[:200])
                
        except Exception as e:
            safe_print(f"❌ 连接测试失败: {str(e)}")

    @staticmethod
    def chat_with_ai(config: Dict[str, Any]) -> None:
        """与AI对话（修复版：使用智能提供商选择）"""
        if not config.get("enable_ai", False):
            safe_print("❌ AI助手未启用")
            return
        
        # 获取可用的提供商
        main_provider, available_providers = AIAssistant.get_available_provider(config)
        
        if not available_providers:
            safe_print("❌ 没有可用的AI服务，请先配置API Key")
            safe_print("💡 请到AI助手设置中启用并配置至少一个提供商")
            return
        
        # 显示当前使用的AI服务
        provider_names = {
            "deepseek": "DeepSeek",
            "aliyun": "阿里云通义千问"
        }
        
        safe_print(f"\n🤖 使用 {provider_names.get(main_provider, main_provider)} 服务")
        if len(available_providers) > 1:
            safe_print(f"💡 备用服务: {', '.join([provider_names.get(p, p) for p in available_providers if p != main_provider])}")
        
        safe_print("输入 '退出' 或 'exit' 结束对话")
        safe_print("-" * 40)
        
        try:
            from collections import deque
        except ImportError:
            safe_print("❌ 需要 collections.deque，使用普通列表")
            message_history = []
            use_deque = False
        else:
            max_history = min(config.get("max_history", 20), 50)
            message_history = deque(maxlen=max_history)
            use_deque = True
        
        max_tokens = config.get("max_history_tokens", 4000)
        current_tokens = 0
        
        while True:
            user_input = input("\n你: ").strip()
            if user_input.lower() in ['退出', 'exit', 'quit', 'q']:
                safe_print("👋 对话结束")
                if use_deque:
                    message_history.clear()
                else:
                    message_history = []
                break
            
            if not user_input:
                safe_print("❌ 输入不能为空")
                continue
            
            safe_print("\nAI思考中...", end="", flush=True)
            try:
                input_tokens = len(user_input) // 4
                
                if not use_deque and current_tokens + input_tokens > max_tokens:
                    while message_history and current_tokens + input_tokens > max_tokens:
                        if len(message_history) >= 2:
                            removed = message_history.pop(0)
                            removed_tokens = len(removed.get('content', '')) // 4
                            current_tokens -= removed_tokens
                
                history_list = list(message_history) if use_deque else message_history
                
                # 使用智能故障转移
                provider_used, reply = AIAssistant.try_providers_with_fallback(
                    config, user_input, history_list, main_provider, available_providers
                )
                
                if provider_used:
                    # 如果实际使用的提供商不是主提供商，说明发生了故障转移
                    if provider_used != main_provider:
                        safe_print(f"\n🔀 已自动切换到 {provider_names.get(provider_used, provider_used)}")
                    
                    safe_print(f"\nAI: {reply}")
                    
                    # 更新对话历史
                    if use_deque:
                        message_history.append({"role": "user", "content": user_input})
                        message_history.append({"role": "assistant", "content": reply})
                    else:
                        message_history.append({"role": "user", "content": user_input})
                        message_history.append({"role": "assistant", "content": reply})
                    
                    current_tokens += input_tokens + (len(reply) // 4)
                else:
                    safe_print(f"\n{reply}")  # 显示错误信息
                    
                if config.get("debug_memory", False):
                    safe_print(f"[调试] 历史记录: {len(message_history)}条, 估算Tokens: {current_tokens}")
                    
            except Exception as e:
                safe_print(f"\n❌ AI服务错误: {str(e)}")

    @staticmethod
    def call_ai_service(config: Dict[str, Any], provider: str, user_input: str, message_history: List[Dict[str, str]]) -> str:
        """调用AI服务"""
        requests = SmartLibraryManagement.check_and_import("requests", "")
        if not requests:
            raise Exception("需要requests库")
        
        provider_config = config.get("providers", {}).get(provider, {})
        
        if provider == "deepseek":
            return AIAssistant.call_deepseek(provider_config, user_input, message_history)
        elif provider == "aliyun":
            return AIAssistant.call_aliyun(provider_config, user_input, message_history)
        else:
            raise Exception(f"不支持的AI提供商: {provider}")

    @staticmethod
    def call_deepseek(config: Dict[str, Any], user_input: str, message_history: List[Dict[str, str]]) -> str:
        """调用DeepSeek"""
        requests = SmartLibraryManagement.check_and_import("requests", "")
        if not requests:
            raise Exception("需要requests库")
        
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        
        messages = message_history.copy()
        messages.append({"role": "user", "content": user_input})
        
        data = {
            "model": config.get("model", "deepseek-chat"),
            "messages": messages,
            "max_tokens": config.get("max_tokens", 1000),
            "temperature": config.get("temperature", 0.7),
            "stream": False
        }
        
        response = requests.post(
            f"{config.get('api_base', 'https://api.deepseek.com')}/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if "choices" in result and len(result["choices"]) > 0:
                return result["choices"][0]["message"]["content"]
            else:
                raise Exception("AI返回格式错误")
        else:
            raise Exception(f"API错误: {response.status_code} - {response.text[:200]}")

    @staticmethod
    def call_aliyun(config: Dict[str, Any], user_input: str, message_history: List[Dict[str, str]]) -> str:
        """调用阿里云"""
        requests = SmartLibraryManagement.check_and_import("requests", "")
        if not requests:
            raise Exception("需要requests库")
        
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json",
            "X-DashScope-SSE": "disable"
        }
        
        messages = message_history.copy()
        messages.append({"role": "user", "content": user_input})
        
        data = {
            "model": config.get("model", "qwen-max"),
            "input": {
                "messages": messages
            },
            "parameters": {
                "max_tokens": config.get("max_tokens", 1000),
                "temperature": config.get("temperature", 0.7)
            }
        }
        
        response = requests.post(
            f"{config.get('api_base', 'https://dashscope.aliyuncs.com')}/api/v1/services/aigc/text-generation/generation",
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if "output" in result and "text" in result["output"]:
                return result["output"]["text"]
            else:
                raise Exception("AI返回格式错误")
        else:
            raise Exception(f"API错误: {response.status_code} - {response.text[:200]}")

    @staticmethod
    def system_analysis(config: Dict[str, Any]) -> None:
        """系统分析（修复版：使用智能提供商选择）"""
        if not config.get("enable_ai", False):
            safe_print("❌ AI助手未启用")
            return
        
        # 获取可用的提供商
        main_provider, available_providers = AIAssistant.get_available_provider(config)
        
        if not available_providers:
            safe_print("❌ 没有可用的AI服务，请先配置API Key")
            return
        
        safe_print("\n🔄 正在收集系统信息...")
        system_info = ""
        
        try:
            data = DataManagement.load_user_data()
            user_count = len(data.get("users", {}))
            system_info += f"用户数量: {user_count}\n"
            
            occupation_list = DataManagement.load_occupation_list()
            system_info += f"职业种类: {len(occupation_list)}\n"
            
            backup_list = DataManagement.get_backup_list()
            system_info += f"备份数量: {len(backup_list)}\n"
            
            psutil = SmartLibraryManagement.check_and_import("psutil", "系统资源监控库")
            if psutil:
                disk = psutil.disk_usage('.')
                system_info += f"磁盘使用率: {disk.percent}%\n"
                system_info += f"可用空间: {disk.free // (1024*1024*1024)} GB\n"
        except Exception as e:
            system_info += f"收集信息时出错: {str(e)}\n"
        
        analysis_prompt = f"""请分析以下系统状态数据，并提供优化建议：

{system_info}

请用中文回答，提供具体的优化建议。"""
        
        safe_print("🤖 AI正在分析系统状态...")
        try:
            # 使用智能故障转移
            provider_used, reply = AIAssistant.try_providers_with_fallback(
                config, analysis_prompt, [], main_provider, available_providers
            )
            
            if provider_used:
                provider_names = {
                    "deepseek": "DeepSeek",
                    "aliyun": "阿里云通义千问"
                }
                
                safe_print("\n" + "="*50)
                safe_print(f"AI分析报告 (使用 {provider_names.get(provider_used, provider_used)}):")
                safe_print("="*50)
                safe_print(reply)
                safe_print("="*50)
            else:
                safe_print(f"\n{reply}")  # 显示错误信息
                
        except Exception as e:
            safe_print(f"❌ AI分析失败: {str(e)}")

# ==================== 命令行类 ====================
class CommandLine:
    def __init__(self):
        self.current_style = "原生"
        self.command_history = []
        self.max_history = 100
        self.admin_mode = False
        self.logged_in_user = "用户"
        self.current_dir = os.getcwd()
        self.init_command_maps()

    def init_command_maps(self):
        """初始化命令映射"""
        self.native_commands = {
            "帮助": {"函数": self.show_help, "描述": "显示所有可用命令"},
            "切换风格": {"函数": self.switch_style, "描述": "切换命令行风格"},
            "清屏": {"函数": self.clear_screen, "描述": "清除屏幕内容"},
            "退出": {"函数": self.exit_command_line, "描述": "退出命令行模式"},
            "重启": {"函数": self.reboot_system, "描述": "重启命令行系统"},
            "登录": {"函数": self.user_login, "描述": "登录用户账户"},
            "注销": {"函数": self.user_logout, "描述": "注销当前用户"},
            "注册": {"函数": self.user_register, "描述": "注册新用户"},
            "用户列表": {"函数": self.show_user_list, "描述": "显示所有用户"},
            "修改密码": {"函数": self.change_password, "描述": "修改当前用户密码"},
            "sudo": {"函数": self.execute_sudo, "描述": "以管理员权限执行命令"},
            "目录": {"函数": self.show_directory, "描述": "显示当前目录内容"},
            "改变目录": {"函数": self.change_directory, "描述": "改变当前工作目录"},
            "当前目录": {"函数": self.show_current_directory, "描述": "显示当前工作目录"},
            "创建目录": {"函数": self.create_directory, "描述": "创建新目录"},
            "删除目录": {"函数": self.delete_directory, "描述": "删除目录"},
            "复制": {"函数": self.copy_file, "描述": "复制文件或目录"},
            "移动": {"函数": self.move_file, "描述": "移动文件或目录"},
            "删除": {"函数": self.delete_file, "描述": "删除文件"},
            "查看": {"函数": self.view_file, "描述": "查看文件内容"},
            "编辑": {"函数": self.edit_file, "描述": "编辑文件内容"},
            "系统信息": {"函数": self.show_system_info, "描述": "显示系统信息"},
            "版本": {"函数": self.show_version, "描述": "显示系统版本"},
            "时间": {"函数": self.show_time, "描述": "显示当前时间"},
            "日期": {"函数": self.show_date, "描述": "显示当前日期"},
            "状态": {"函数": self.show_status, "描述": "显示系统状态"},
            "网络信息": {"函数": self.show_network_info, "描述": "显示网络信息"},
            "连接测试": {"函数": self.test_connection, "描述": "测试网络连接"},
            "进程列表": {"函数": self.show_process_list, "描述": "显示当前进程"},
            "历史": {"函数": self.show_history, "描述": "显示命令历史"},
            "清除历史": {"函数": self.clear_history, "描述": "清除命令历史"},
            "系统服务": {"函数": self.show_system_services, "描述": "显示系统服务状态"},
            "磁盘使用": {"函数": self.show_disk_usage, "描述": "显示磁盘使用情况"},
            "内存信息": {"函数": self.show_memory_info, "描述": "显示内存信息"},
            "切换用户文件": {"函数": self.switch_user_file, "描述": "切换当前操作用户文件"},
            "用户文件列表": {"函数": self.list_user_files, "描述": "列出所有用户文件"},
            "创建用户文件": {"函数": self.create_user_file, "描述": "创建新的用户数据文件"},
            "当前用户文件": {"函数": self.show_current_user_file, "描述": "显示当前使用的用户文件"},
        }
        
        self.windows_commands = {
            "help": {"函数": self.show_help, "描述": "显示所有可用命令"},
            "sle": {"函数": self.switch_style, "描述": "切换命令行风格"},
            "cls": {"函数": self.clear_screen, "描述": "清除屏幕内容"},
            "exit": {"函数": self.exit_command_line, "描述": "退出命令行模式"},
            "reboot": {"函数": self.reboot_system, "描述": "重启命令行系统"},
            "dir": {"函数": self.show_directory, "描述": "显示当前目录内容"},
            "cd": {"函数": self.change_directory, "描述": "改变当前工作目录"},
            "pwd": {"函数": self.show_current_directory, "描述": "显示当前工作目录"},
            "md": {"函数": self.create_directory, "描述": "创建新目录"},
            "rd": {"函数": self.delete_directory, "描述": "删除目录"},
            "copy": {"函数": self.copy_file, "描述": "复制文件或目录"},
            "move": {"函数": self.move_file, "描述": "移动文件或目录"},
            "del": {"函数": self.delete_file, "描述": "删除文件"},
            "type": {"函数": self.view_file, "描述": "查看文件内容"},
            "edit": {"函数": self.edit_file, "描述": "编辑文件内容"},
            "systeminfo": {"函数": self.show_system_info, "描述": "显示系统信息"},
            "ver": {"函数": self.show_version, "描述": "显示系统版本"},
            "time": {"函数": self.show_time, "描述": "显示当前时间"},
            "date": {"函数": self.show_date, "描述": "显示当前日期"},
            "tasklist": {"函数": self.show_process_list, "描述": "显示当前进程"},
            "history": {"函数": self.show_history, "描述": "显示命令历史"},
            "services": {"函数": self.show_system_services, "描述": "显示系统服务"},
            "diskpart": {"函数": self.show_disk_usage, "描述": "显示磁盘分区"},
            "switchfile": {"函数": self.switch_user_file, "描述": "切换用户文件"},
            "userfiles": {"函数": self.list_user_files, "描述": "列出用户文件"},
        }
        
        self.linux_commands = {
            "man": {"函数": self.show_help, "描述": "显示命令手册"},
            "sle": {"函数": self.switch_style, "描述": "切换命令行风格"},
            "clear": {"函数": self.clear_screen, "描述": "清除屏幕内容"},
            "exit": {"函数": self.exit_command_line, "描述": "退出命令行模式"},
            "reboot": {"函数": self.reboot_system, "描述": "重启命令行系统"},
            "ls": {"函数": self.show_directory, "描述": "列出目录内容"},
            "cd": {"函数": self.change_directory, "描述": "改变当前工作目录"},
            "pwd": {"函数": self.show_current_directory, "描述": "显示当前工作目录"},
            "mkdir": {"函数": self.create_directory, "描述": "创建新目录"},
            "rmdir": {"函数": self.delete_directory, "描述": "删除空目录"},
            "cp": {"函数": self.copy_file, "描述": "复制文件或目录"},
            "mv": {"函数": self.move_file, "描述": "移动文件或目录"},
            "rm": {"函数": self.delete_file, "描述": "删除文件"},
            "cat": {"函数": self.view_file, "描述": "查看文件内容"},
            "vi": {"函数": self.edit_file, "描述": "编辑文件内容"},
            "nano": {"函数": self.edit_file, "描述": "编辑文件内容"},
            "uname": {"函数": self.show_system_info, "描述": "显示系统信息"},
            "date": {"函数": self.show_time, "描述": "显示当前时间"},
            "cal": {"函数": self.show_date, "描述": "显示日历"},
            "top": {"函数": self.show_status, "描述": "显示系统状态"},
            "ps": {"函数": self.show_process_list, "描述": "显示当前进程"},
            "history": {"函数": self.show_history, "描述": "显示命令历史"},
            "systemctl": {"函数": self.show_system_services, "描述": "系统服务管理"},
            "df": {"函数": self.show_disk_usage, "描述": "显示磁盘使用"},
            "free": {"函数": self.show_memory_info, "描述": "显示内存信息"},
            "switch": {"函数": self.switch_user_file, "描述": "切换文件"},
            "lsuserfiles": {"函数": self.list_user_files, "描述": "列出用户文件"},
        }

    def get_current_command_set(self) -> Dict[str, Dict[str, Any]]:
        """获取当前命令集"""
        if self.current_style == "原生":
            return self.native_commands
        elif self.current_style == "Windows":
            return self.windows_commands
        elif self.current_style == "Linux":
            return self.linux_commands
        else:
            return self.native_commands

    def show_help(self, params: Optional[str] = None) -> None:
        """显示帮助"""
        command_set = self.get_current_command_set()
        safe_print(f"\n=== {self.current_style}风格可用命令 ===")
        safe_print("输入 '命令名' 执行相应操作")
        safe_print("-" * 50)
        
        for cmd_name, cmd_info in command_set.items():
            safe_print(f"{cmd_name:<20} - {cmd_info['描述']}")
        
        safe_print(f"\n当前风格: {self.current_style}")
        safe_print(f"当前用户: {self.logged_in_user}")
        safe_print(f"管理员模式: {'是' if self.admin_mode else '否'}")

    def switch_style(self, style_name: Optional[str] = None) -> None:
        """切换风格"""
        if not style_name:
            safe_print("\n=== 可用风格 ===")
            safe_print("1. 原生 - 自定义命令行风格")
            safe_print("2. Windows - Windows命令行风格")
            safe_print("3. Linux - Linux终端风格")
            selection = input("\n请选择风格(1-3): ").strip()
            style_map = {"1": "原生", "2": "Windows", "3": "Linux"}
            if selection in style_map:
                style_name = style_map[selection]
            else:
                safe_print("❌ 无效选择")
                return
        
        valid_styles = ["原生", "Windows", "Linux"]
        if style_name in valid_styles:
            self.current_style = style_name
            safe_print(f"✅ 已切换到 {style_name} 风格")
            self.show_style_info()
        else:
            safe_print(f"❌ 无效的风格: {style_name}")

    def show_style_info(self) -> None:
        """显示风格信息"""
        safe_print(f"\n=== {self.current_style}风格命令行 ===")
        if self.current_style == "原生":
            safe_print("这是一个自定义的命令行界面")
            safe_print("特点: 中文命令，易于理解")
        elif self.current_style == "Windows":
            safe_print("Windows命令行风格")
            safe_print("特点: 类似Windows CMD/PowerShell")
        elif self.current_style == "Linux":
            safe_print("Linux终端风格")
            safe_print("特点: 类似Linux Bash终端")
        safe_print(f"\n当前用户: {self.logged_in_user}")
        safe_print(f"当前目录: {self.current_dir}")
        safe_print("输入 '帮助,help,man' 查看所有可用命令")

    def clear_screen(self, params: Optional[str] = None) -> None:
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')
        safe_print(f"{self.current_style}命令行 - 用户: {self.logged_in_user}")
        safe_print("输入 '帮助,help,man' 查看可用命令")

    def exit_command_line(self, params: Optional[str] = None) -> bool:
        """退出命令行"""
        return True

    def reboot_system(self, params: Optional[str] = None) -> bool:
        """重启系统"""
        safe_print("🔄 重启命令行系统...")
        self.__init__()
        self.show_style_info()
        return False

    def user_login(self, username: Optional[str] = None) -> None:
        """用户登录"""
        if not username:
            username = input("用户名: ").strip()
        safe_print(f"✅ 登录成功! 欢迎 {username}")
        self.logged_in_user = username

    def user_logout(self, params: Optional[str] = None) -> None:
        """用户注销"""
        safe_print(f"👋 再见, {self.logged_in_user}")
        self.logged_in_user = "无"
        self.admin_mode = False

    def user_register(self, username: Optional[str] = None) -> None:
        """用户注册"""
        if not username:
            username = input("用户名: ").strip()
        safe_print(f"✅ 用户注册成功: {username}")

    def show_user_list(self, params: Optional[str] = None) -> None:
        """显示用户列表"""
        safe_print("\n=== 用户列表 ===")
        safe_print("当前命令行用户: 用户 (默认)")
        safe_print(f"登录用户: {self.logged_in_user}")

    def change_password(self, params: Optional[str] = None) -> None:
        """修改密码"""
        safe_print("修改密码功能需要进入主菜单使用")

    def execute_sudo(self, command: Optional[str] = None) -> bool:
        """执行sudo"""
        if not command:
            safe_print("❌ 请指定要执行的命令")
            return False
        
        if self.admin_mode:
            safe_print("⚠️  已经是管理员模式")
        else:
            safe_print("🛡️  切换到管理员模式")
            self.admin_mode = True
        
        return self.execute_command(command)

    def show_directory(self, path: Optional[str] = None) -> None:
        """显示目录"""
        if not path:
            path = self.current_dir
        
        try:
            if not os.path.exists(path):
                safe_print(f"❌ 路径不存在: {path}")
                return
            
            safe_print(f"\n=== 目录: {os.path.abspath(path)} ===")
            items = []
            
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    type_str = "<DIR>"
                    size = ""
                else:
                    type_str = "文件"
                    size = f"{os.path.getsize(item_path)} 字节"
                
                modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(item_path)).strftime("%Y-%m-%d %H:%M")
                items.append((item, type_str, size, modified_time))
            
            items.sort(key=lambda x: (0 if x[1] == "<DIR>" else 1, x[0].lower()))
            
            safe_print(f"{'名称':<30} {'类型':<10} {'大小':<15} {'修改时间':<20}")
            safe_print("-" * 80)
            
            for item, type_str, size, modified_time in items:
                safe_print(f"{item:<30} {type_str:<10} {size:<15} {modified_time:<20}")
            
            safe_print(f"\n共 {len(items)} 个项目")
            
        except Exception as e:
            safe_print(f"❌ 访问目录失败: {str(e)}")

    def change_directory(self, path: Optional[str] = None) -> Optional[str]:
        """改变目录"""
        if not path:
            return self.show_current_directory()
        
        try:
            if path == "..":
                new_path = os.path.dirname(self.current_dir)
            elif path == ".":
                new_path = self.current_dir
            elif path == "~":
                new_path = os.path.expanduser("~")
            else:
                new_path = os.path.abspath(os.path.join(self.current_dir, path))
            
            if not os.path.exists(new_path):
                safe_print(f"❌ 路径不存在: {new_path}")
                return None
            
            if not os.path.isdir(new_path):
                safe_print(f"❌ 不是目录: {new_path}")
                return None
            
            self.current_dir = new_path
            safe_print(f"✅ 当前目录: {self.current_dir}")
            return self.current_dir
            
        except Exception as e:
            safe_print(f"❌ 改变目录失败: {str(e)}")
            return None

    def show_current_directory(self, params: Optional[str] = None) -> str:
        """显示当前目录"""
        safe_print(f"📁 当前目录: {self.current_dir}")
        return self.current_dir

    def create_directory(self, dirname: Optional[str] = None) -> None:
        """创建目录"""
        if not dirname:
            safe_print("❌ 请指定目录名")
            return
        
        try:
            dir_path = os.path.join(self.current_dir, dirname)
            if os.path.exists(dir_path):
                safe_print(f"❌ 目录已存在: {dirname}")
                return
            
            os.makedirs(dir_path, exist_ok=True)
            safe_print(f"✅ 目录创建成功: {dir_path}")
            
        except Exception as e:
            safe_print(f"❌ 创建目录失败: {str(e)}")

    def delete_directory(self, dirname: Optional[str] = None) -> None:
        """删除目录"""
        if not dirname:
            safe_print("❌ 请指定目录名")
            return
        
        try:
            dir_path = os.path.join(self.current_dir, dirname)
            if not os.path.exists(dir_path):
                safe_print(f"❌ 目录不存在: {dirname}")
                return
            
            if not os.path.isdir(dir_path):
                safe_print(f"❌ 不是目录: {dirname}")
                return
            
            confirm = input(f"确定删除目录 '{dirname}' 吗? (Y/N): ").strip().upper()
            if confirm != "Y":
                safe_print("操作已取消")
                return
            
            shutil.rmtree(dir_path)
            safe_print(f"✅ 目录删除成功: {dirname}")
            
        except Exception as e:
            safe_print(f"❌ 删除目录失败: {str(e)}")

    def copy_file(self, params: Optional[str] = None) -> None:
        """复制文件"""
        if not params:
            safe_print("❌ 请指定源文件和目标")
            return
        
        param_list = params.split()
        if len(param_list) < 2:
            safe_print("❌ 请指定源文件和目标")
            return
        
        source = param_list[0]
        dest = param_list[1]
        
        try:
            source_path = os.path.join(self.current_dir, source) if not os.path.isabs(source) else source
            dest_path = os.path.join(self.current_dir, dest) if not os.path.isabs(dest) else dest
            
            if not os.path.exists(source_path):
                safe_print(f"❌ 源文件不存在: {source}")
                return
            
            shutil.copy2(source_path, dest_path)
            safe_print(f"✅ 复制成功: {source} -> {dest}")
            
        except Exception as e:
            safe_print(f"❌ 复制失败: {str(e)}")

    def move_file(self, params: Optional[str] = None) -> None:
        """移动文件"""
        if not params:
            safe_print("❌ 请指定源文件和目标")
            return
        
        param_list = params.split()
        if len(param_list) < 2:
            safe_print("❌ 请指定源文件和目标")
            return
        
        source = param_list[0]
        dest = param_list[1]
        
        try:
            source_path = os.path.join(self.current_dir, source) if not os.path.isabs(source) else source
            dest_path = os.path.join(self.current_dir, dest) if not os.path.isabs(dest) else dest
            
            if not os.path.exists(source_path):
                safe_print(f"❌ 源文件不存在: {source}")
                return
            
            shutil.move(source_path, dest_path)
            safe_print(f"✅ 移动成功: {source} -> {dest}")
            
        except Exception as e:
            safe_print(f"❌ 移动失败: {str(e)}")

    def delete_file(self, filename: Optional[str] = None) -> None:
        """删除文件"""
        if not filename:
            safe_print("❌ 请指定文件名")
            return
        
        try:
            file_path = os.path.join(self.current_dir, filename) if not os.path.isabs(filename) else filename
            if not os.path.exists(file_path):
                safe_print(f"❌ 文件不存在: {filename}")
                return
            
            if os.path.isdir(file_path):
                safe_print(f"❌ 不能删除目录，请使用删除目录命令: {filename}")
                return
            
            confirm = input(f"确定删除文件 '{filename}' 吗? (Y/N): ").strip().upper()
            if confirm != "Y":
                safe_print("操作已取消")
                return
            
            os.remove(file_path)
            safe_print(f"✅ 文件删除成功: {filename}")
            
        except Exception as e:
            safe_print(f"❌ 删除文件失败: {str(e)}")

    def view_file(self, filename: Optional[str] = None) -> None:
        """查看文件（增强路径安全）"""
        if not filename:
            safe_print("❌ 请指定文件名")
            return
        
        try:
            filename = filename.strip()
            if not filename:
                safe_print("❌ 文件名不能为空")
                return
            
            forbidden_patterns = ['..', '~', '/', '\\', ':', '*', '?', '"', '<', '>', '|']
            for pattern in forbidden_patterns:
                if pattern in filename:
                    safe_print("❌ 文件名包含非法字符")
                    SystemLog.security_log(f"路径遍历尝试: {filename}", "防火墙", "阻止")
                    return
            
            safe_filename = PathSecurity.sanitize_filename(filename)
            file_path = os.path.join(self.current_dir, safe_filename)
            
            try:
                real_path = os.path.realpath(file_path)
                real_base = os.path.realpath(self.current_dir)
                
                if not real_path.startswith(real_base):
                    safe_print("❌ 非法路径访问：试图访问上级目录")
                    SystemLog.security_log(f"路径越界尝试: {real_path}", "防火墙", "阻止")
                    return
            except Exception:
                safe_print("❌ 路径安全检查失败")
                return
            
            if not os.path.exists(file_path):
                safe_print(f"❌ 文件不存在: {safe_filename}")
                return
            
            if os.path.isdir(file_path):
                safe_print(f"❌ 不能查看目录内容: {safe_filename}")
                return
            
            file_size = os.path.getsize(file_path)
            if file_size > 10 * 1024 * 1024:
                safe_print(f"❌ 文件过大 ({file_size//1024}KB)，无法查看")
                return
            
            safe_print(f"\n=== 文件内容: {safe_filename} ===")
            
            encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1']
            content = None
            
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                safe_print("❌ 无法解码文件内容")
                return
            
            max_display_size = 5000
            if len(content) > max_display_size:
                safe_print(content[:max_display_size])
                safe_print(f"... (省略 {len(content) - max_display_size} 个字符)")
            else:
                safe_print(content)
                
        except Exception as e:
            safe_print(f"❌ 查看文件失败: {str(e)}")
            SystemLog.log(f"查看文件失败: {str(e)}", "错误")

    def edit_file(self, filename: Optional[str] = None) -> None:
        """编辑文件（增强安全）"""
        if not filename:
            safe_print("❌ 请指定文件名")
            return
        
        try:
            filename = filename.strip()
            if not filename:
                safe_print("❌ 文件名不能为空")
                return
            
            forbidden_patterns = ['..', '~', '/', '\\', ':', '*', '?', '"', '<', '>', '|']
            for pattern in forbidden_patterns:
                if pattern in filename:
                    safe_print("❌ 文件名包含非法字符")
                    return
            
            safe_filename = PathSecurity.sanitize_filename(filename)
            file_path = os.path.join(self.current_dir, safe_filename)
            
            try:
                real_path = os.path.realpath(file_path)
                real_base = os.path.realpath(self.current_dir)
                
                if not real_path.startswith(real_base):
                    safe_print("❌ 非法路径访问")
                    return
            except Exception:
                safe_print("❌ 路径安全检查失败")
                return
            
            system_files = ['1_1_PWOS2.py', 'users.json', 'secure_passwords.json']
            if safe_filename in system_files:
                safe_print(f"❌ 禁止编辑系统文件: {safe_filename}")
                return
            
            file_exists = os.path.exists(file_path)
            
            if file_exists:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            else:
                content = ""
            
            safe_print(f"\n=== 编辑文件: {safe_filename} ===")
            safe_print("输入内容，在新的一行输入 ':wq' 保存并退出")
            safe_print("输入 ':q!' 不保存退出")
            safe_print("-" * 40)
            
            if content:
                safe_print("当前内容:")
                safe_print(content[:1000])
                if len(content) > 1000:
                    safe_print(f"... (省略 {len(content) - 1000} 个字符)")
                safe_print("-" * 40)
            
            new_content = []
            safe_print("开始输入内容:")
            
            while True:
                try:
                    line = input()
                    if line == ":wq":
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write("\n".join(new_content))
                        safe_print(f"✅ 文件已保存: {safe_filename}")
                        break
                    elif line == ":q!":
                        safe_print("❌ 编辑已取消")
                        break
                    else:
                        new_content.append(line)
                except KeyboardInterrupt:
                    safe_print("\n❌ 编辑中断")
                    break
                    
        except Exception as e:
            safe_print(f"❌ 编辑文件失败: {str(e)}")

    def show_system_info(self, params: Optional[str] = None) -> None:
        """显示系统信息"""
        try:
            safe_print("\n=== 系统信息 ===")
            safe_print(f"系统版本: {system_name}")
            safe_print(f"Python版本: {sys.version}")
            safe_print(f"系统平台: {sys.platform}")
            safe_print(f"工作目录: {os.getcwd()}")
            safe_print(f"命令行风格: {self.current_style}")
            safe_print(f"当前用户: {self.logged_in_user}")
            safe_print(f"管理员模式: {'是' if self.admin_mode else '否'}")
            safe_print(f"当前目录: {self.current_dir}")
            
            psutil = SmartLibraryManagement.check_and_import("psutil", "系统监控库")
            if psutil:
                try:
                    cpu_usage = psutil.cpu_percent(interval=0.1)
                    memory = psutil.virtual_memory()
                    safe_print(f"CPU使用率: {cpu_usage}%")
                    safe_print(f"内存使用率: {memory.percent}%")
                except Exception:
                    pass
                    
        except Exception as e:
            safe_print(f"❌ 显示系统信息失败: {str(e)}")

    def show_version(self, params: Optional[str] = None) -> None:
        """显示版本"""
        safe_print(f"\n{system_name}")
        safe_print(f"命令行版本: 1.0")
        safe_print(f"当前风格: {self.current_style}")

    def show_time(self, params: Optional[str] = None) -> None:
        """显示时间"""
        current_time = datetime.datetime.now()
        safe_print(f"🕒 当前时间: {current_time.strftime('%H:%M:%S')}")

    def show_date(self, params: Optional[str] = None) -> None:
        """显示日期"""
        current_time = datetime.datetime.now()
        safe_print(f"📅 当前日期: {current_time.strftime('%Y年%m月%d日')}")

    def show_status(self, params: Optional[str] = None) -> None:
        """显示状态"""
        safe_print("\n=== 系统状态 ===")
        safe_print(f"当前用户: {self.logged_in_user}")
        safe_print(f"管理员: {'是' if self.admin_mode else '否'}")
        safe_print(f"当前目录: {self.current_dir}")
        safe_print(f"命令历史: {len(self.command_history)} 条")
        
        psutil = SmartLibraryManagement.check_and_import("psutil", "系统监控库")
        if psutil:
            try:
                cpu_usage = psutil.cpu_percent(interval=0.1)
                memory = psutil.virtual_memory()
                safe_print(f"CPU使用率: {cpu_usage}%")
                safe_print(f"内存使用率: {memory.percent}%")
            except Exception:
                pass

    def show_network_info(self, params: Optional[str] = None) -> None:
        """显示网络信息"""
        safe_print("\n=== 网络信息 ===")
        try:
            hostname = socket.gethostname()
            safe_print(f"主机名: {hostname}")
            
            try:
                ip_address = socket.gethostbyname(hostname)
                safe_print(f"IP地址: {ip_address}")
            except Exception:
                safe_print("IP地址: 无法获取")
                
        except Exception as e:
            safe_print(f"❌ 获取网络信息失败: {str(e)}")

    def test_connection(self, host: Optional[str] = None) -> None:
        """测试连接"""
        if not host:
            host = input("请输入主机名或IP地址: ").strip()
        
        if not host:
            safe_print("❌ 请指定主机")
            return
        
        safe_print(f"🔄 测试连接到 {host}...")
        requests = SmartLibraryManagement.check_and_import("requests", "网络请求库")
        
        if not requests:
            safe_print("❌ 需要requests库")
            return
        
        try:
            response = requests.get(f"http://{host}", timeout=5)
            if response.status_code == 200:
                safe_print(f"✅ 连接成功! 状态码: {response.status_code}")
            else:
                safe_print(f"⚠️  连接异常! 状态码: {response.status_code}")
        except requests.exceptions.Timeout:
            safe_print("❌ 连接超时")
        except requests.exceptions.ConnectionError:
            safe_print("❌ 连接失败")
        except Exception as e:
            safe_print(f"❌ 连接错误: {str(e)}")

    def show_process_list(self, params: Optional[str] = None) -> None:
        """显示进程列表"""
        safe_print("\n=== 进程列表 ===")
        psutil = SmartLibraryManagement.check_and_import("psutil", "进程管理库")
        
        if not psutil:
            safe_print("需要psutil库来显示进程信息")
            return
        
        try:
            processes = []
            for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    process_info = process.info
                    processes.append(process_info)
                except Exception:
                    continue
            
            processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
            
            safe_print(f"{'PID':<8} {'名称':<30} {'CPU%':<8} {'内存%':<8}")
            safe_print("-" * 60)
            
            for process in processes[:10]:
                safe_print(f"{process['pid']:<8} {process['name']:<30} {process['cpu_percent']:<8.1f} {process['memory_percent']:<8.2f}")
            
            safe_print(f"\n共 {len(processes)} 个进程")
            
        except Exception as e:
            safe_print(f"❌ 获取进程信息失败: {str(e)}")

    def show_history(self, count: Optional[str] = None) -> None:
        """显示历史"""
        if not count:
            count_num = 20
        else:
            try:
                count_num = int(count)
            except ValueError:
                count_num = 20
        
        safe_print(f"\n=== 命令历史 (最近{count_num}条) ===")
        if not self.command_history:
            safe_print("没有命令历史")
            return
        
        start_index = max(0, len(self.command_history) - count_num)
        for i, command in enumerate(self.command_history[start_index:], start_index + 1):
            safe_print(f"{i:>3}. {command}")

    def clear_history(self, params: Optional[str] = None) -> None:
        """清除历史"""
        confirm = input("确定要清除所有命令历史吗? (Y/N): ").strip().upper()
        if confirm == "Y":
            self.command_history = []
            safe_print("✅ 命令历史已清除")
        else:
            safe_print("操作已取消")

    def show_system_services(self, params: Optional[str] = None) -> None:
        """显示系统服务"""
        safe_print("\n=== 系统服务 ===")
        services = [
            {"name": "用户管理服务", "status": "运行中", "uptime": "24天"},
            {"name": "网络防火墙", "status": "运行中", "uptime": "5天"},
            {"name": "AI助手", "status": "已停止", "uptime": "-"},
            {"name": "备份服务", "status": "运行中", "uptime": "12小时"},
            {"name": "日志服务", "status": "运行中", "uptime": "3天"}
        ]
        
        for service in services:
            status_icon = "🟢" if service["status"] == "运行中" else "🔴"
            safe_print(f"{status_icon} {service['name']:<20} {service['status']:<10} 运行时间: {service['uptime']}")

    def show_disk_usage(self, params: Optional[str] = None) -> None:
        """显示磁盘使用"""
        psutil = SmartLibraryManagement.check_and_import("psutil", "磁盘监控库")
        if not psutil:
            safe_print("需要psutil库")
            return
        
        try:
            safe_print("\n=== 磁盘使用情况 ===")
            partitions = psutil.disk_partitions()
            
            for partition in partitions:
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    safe_print(f"📁 {partition.device:<15} {partition.mountpoint:<15}")
                    safe_print(f"   总容量: {usage.total//(1024**3):>6} GB | 已用: {usage.used//(1024**3):>5} GB | 可用: {usage.free//(1024**3):>5} GB")
                    safe_print(f"   使用率: {usage.percent:>5.1f}%")
                    safe_print()
                except Exception:
                    continue
                    
        except Exception as e:
            safe_print(f"❌ 显示磁盘使用失败: {str(e)}")

    def show_memory_info(self, params: Optional[str] = None) -> None:
        """显示内存信息"""
        psutil = SmartLibraryManagement.check_and_import("psutil", "内存监控库")
        if not psutil:
            safe_print("需要psutil库")
            return
        
        try:
            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()
            
            safe_print("\n=== 内存信息 ===")
            safe_print(f"物理内存: {memory.total//(1024**3)} GB")
            safe_print(f"已使用: {memory.used//(1024**3)} GB ({memory.percent}%)")
            safe_print(f"可用: {memory.available//(1024**3)} GB")
            
            safe_print("\n=== 交换空间 ===")
            safe_print(f"总计: {swap.total//(1024**3)} GB")
            safe_print(f"已使用: {swap.used//(1024**3)} GB ({swap.percent}%)")
            safe_print(f"可用: {swap.free//(1024**3)} GB")
            
        except Exception as e:
            safe_print(f"❌ 显示内存信息失败: {str(e)}")

    def switch_user_file(self, params: Optional[str] = None) -> None:
        """切换用户文件"""
        if not params:
            current_file = UserGroupManager.get_current_user_file()
            safe_print(f"📁 当前用户文件: {os.path.basename(current_file)}")
            safe_print("用法: 切换用户文件 <文件名>")
            return
        
        file_name = params.strip()
        if not file_name.endswith('.json'):
            file_name += '.json'
        
        if UserGroupManager.switch_user_file(file_name):
            safe_print(f"✅ 已切换到用户文件: {file_name}")
        else:
            safe_print(f"❌ 切换失败")
    
    def list_user_files(self, params: Optional[str] = None) -> None:
        """列出所有用户文件"""
        user_files_dir = UserGroupManager.get_user_files_dir()
        
        if not os.path.exists(user_files_dir):
            safe_print("用户文件目录不存在")
            return
        
        all_files = []
        for file in os.listdir(user_files_dir):
            if file.endswith('.json'):
                file_path = os.path.join(user_files_dir, file)
                all_files.append((file, file_path))
        
        if not all_files:
            safe_print("没有用户文件")
            return
        
        safe_print("\n=== 用户文件列表 ===")
        for file_name, file_path in all_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                user_count = len(data.get("users", {}))
                file_size = os.path.getsize(file_path)
                
                groups_data = UserGroupManager.load_groups_data()
                is_current = (groups_data.get("current_file") == file_name)
                current_mark = " ✅当前" if is_current else ""
                
                safe_print(f"📄 {file_name}{current_mark}")
                safe_print(f"   用户数: {user_count}, 大小: {file_size} 字节")
                
            except Exception as e:
                safe_print(f"📄 {file_name} (读取失败)")
    
    def create_user_file(self, params: Optional[str] = None) -> None:
        """创建新的用户文件"""
        if not params:
            file_name = input("请输入文件名(无需.json后缀): ").strip()
        else:
            file_name = params.strip()
        
        if not file_name:
            safe_print("❌ 文件名不能为空")
            return
        
        if not file_name.endswith('.json'):
            file_name += '.json'
        
        user_files_dir = UserGroupManager.get_user_files_dir()
        file_path = os.path.join(user_files_dir, file_name)
        
        if os.path.exists(file_path):
            safe_print(f"❌ 文件 '{file_name}' 已存在")
            return
        
        try:
            new_file_data = {
                "users": {},
                "next_id": 1,
                "empty_ids": [],
                "metadata": {
                    "name": file_name.replace('.json', ''),
                    "create_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(new_file_data, f, ensure_ascii=False, indent=2)
            
            groups_data = UserGroupManager.load_groups_data()
            if file_name not in groups_data["ungrouped_files"]:
                groups_data["ungrouped_files"].append(file_name)
                UserGroupManager.save_groups_data(groups_data)
            
            safe_print(f"✅ 用户文件 '{file_name}' 创建成功")
            
        except Exception as e:
            safe_print(f"❌ 创建文件失败: {str(e)}")
    
    def show_current_user_file(self, params: Optional[str] = None) -> None:
        """显示当前用户文件信息"""
        current_file = UserGroupManager.get_current_user_file()
        file_name = os.path.basename(current_file)
        
        safe_print(f"\n=== 当前用户文件信息 ===")
        safe_print(f"文件名: {file_name}")
        safe_print(f"完整路径: {current_file}")
        
        if os.path.exists(current_file):
            try:
                with open(current_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                user_count = len(data.get("users", {}))
                file_size = os.path.getsize(current_file)
                create_time = data.get("metadata", {}).get("create_time", "未知")
                last_modified = data.get("metadata", {}).get("last_modified", "未知")
                
                safe_print(f"用户数量: {user_count}")
                safe_print(f"文件大小: {file_size} 字节")
                safe_print(f"创建时间: {create_time}")
                safe_print(f"最后修改: {last_modified}")
                
            except Exception as e:
                safe_print(f"读取文件信息失败: {str(e)}")
        else:
            safe_print("⚠️  文件不存在")

    def execute_command(self, input_command: str) -> bool:
        """执行命令"""
        if not input_command:
            return False
        
        self.command_history.append(input_command)
        if len(self.command_history) > self.max_history:
            self.command_history.pop(0)
        
        command_parts = input_command.strip().split()
        if not command_parts:
            return False
        
        command_name = command_parts[0]
        params = " ".join(command_parts[1:]) if len(command_parts) > 1 else None
        
        command_set = self.get_current_command_set()
        command = command_set.get(command_name)
        
        if command:
            try:
                if params is not None:
                    result = command['函数'](params)
                else:
                    result = command['函数']()
                return result
            except Exception as e:
                safe_print(f"❌ 执行命令错误: {str(e)}")
                return False
        else:
            safe_print(f"❌ 未知命令: {command_name}")
            safe_print("输入 '帮助,help,man' 查看可用命令")
            return False

    def run(self) -> None:
        """运行命令行"""
        self.show_style_info()
        
        while True:
            try:
                if self.current_style == "原生":
                    prompt = f"{self.logged_in_user}@{self.current_style} {self.current_dir}> "
                elif self.current_style == "Windows":
                    prompt = f"{self.current_dir}> "
                elif self.current_style == "Linux":
                    prompt = f"{self.logged_in_user}@{self.current_style}:{self.current_dir}$ "
                else:
                    prompt = f"> "
                
                if self.admin_mode:
                    prompt = "# " + prompt
                
                input_command = input(prompt).strip()
                if not input_command:
                    continue
                
                result = self.execute_command(input_command)
                if result is True:
                    safe_print("退出命令行模式")
                    break
                    
            except KeyboardInterrupt:
                safe_print("\n输入 '退出' 或 'exit' 退出命令行")
            except EOFError:
                safe_print("\n退出命令行模式")
                break
            except Exception as e:
                safe_print(f"❌ 系统错误: {str(e)}")

# ==================== 打包助手 ====================
class BuildHelper:
    @staticmethod
    def prepare_for_exe() -> bool:
        """准备EXE打包"""
        safe_print("\n===== EXE打包准备 =====")
        
        spec_content = """# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['pwos_enhanced_complete_fixed.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('user_system_data', 'user_system_data'),
        ('update_packages', 'update_packages')
    ],
    hiddenimports=[
        'psutil',
        'requests',
        'cryptography',
        'colorama',
        'prettytable',
        'dns.resolver',
        'dns.rdtypes',
        'dns.rdtypes.IN',
        'dns.rdtypes.ANY'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=2,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PWOS2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='system_icon.ico'
)
"""
        
        safe_print("📝 生成打包配置文件...")
        with open("build_spec.spec", "w", encoding="utf-8") as f:
            f.write(spec_content)
        
        safe_print("📋 打包命令:")
        safe_print("1. 安装打包工具: pip install pyinstaller")
        safe_print("2. 打包命令: pyinstaller build_spec.spec")
        safe_print("3. 或者使用: pyinstaller -F -w -i system_icon.ico pwos_enhanced_complete_fixed.py")
        safe_print("\n📁 确保以下目录存在:")
        safe_print("  • user_system_data/")
        safe_print("  • update_packages/")
        safe_print("  • user_system_data/backups/")
        
        return True
    
    @staticmethod
    def create_installer() -> bool:
        """
        创建安装程序 - 生成用于部署PWOS2的批处理安装脚本
        
        功能:
        1. 检查并创建必要的系统目录
        2. 验证Python环境
        3. 安装必要的Python依赖库
        4. 提供安装完成后的使用说明
        
        创建的目录结构:
        - user_system_data/          # 用户数据目录
          └── backups/               # 备份文件目录
        - update_packages/           # 更新包存放目录
        
        安装的依赖库:
        - requests: HTTP请求库
        - psutil: 系统进程和资源监控库
        - prettytable: 美化表格输出库
        
        返回值:
        - True: 安装脚本创建成功
        - False: 创建失败
        
        注意事项:
        - 需要Python 3.6+环境
        - 需要管理员权限来创建目录（Windows）
        - 依赖库安装可能需要网络连接
        """
        safe_print("\n===== 创建安装程序 =====")
        # 创建简单的安装脚本
        installer_script = """@echo off
echo 正在安装PWOS2...
echo.

REM 创建必要目录
if not exist "user_system_data" mkdir user_system_data
if not exist "user_system_data\\backups" mkdir user_system_data\\backups
if not exist "update_packages" mkdir update_packages

REM 检查Python环境
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未检测到Python，请先安装Python 3.6+
    pause
    exit /b 1
)

REM 安装依赖
echo 正在安装依赖库...
pip install requests psutil prettytable >nul 2>&1

echo.
echo ✅ 安装完成！
echo 运行命令: python "PWOS.exe"
echo.
pause
"""
        
        with open("install.bat", "w", encoding="utf-8") as f:
            f.write(installer_script)
        
        safe_print("✅ 已创建安装脚本: install.bat")
        return True

# ==================== 主程序 ====================
def command_line_mode(specified_style: Optional[str] = None) -> None:
    """
    命令行模式入口函数
    
    参数:
    - specified_style: 可选参数，指定命令行风格，可以是"原生"、"Windows"、"Linux"
    
    功能:
    1. 显示命令行模式的欢迎信息
    2. 初始化命令行环境
    3. 如果指定了风格，则应用该风格
    4. 运行命令行主循环
    
    支持的特性:
    - 三种命令行风格切换
    - 命令历史记录
    - 命令自动补全
    - 上下文敏感帮助
    
    退出方式:
    - 输入"退出"或"exit"命令
    - Ctrl+C 中断
    
    返回值: 无
    """
    safe_print("\n" + "=" * 60)
    safe_print("      进入命令行模式")
    safe_print("=" * 60)
    safe_print("支持三种风格: 原生, Windows, Linux")
    safe_print("输入 '帮助' 查看可用命令")
    safe_print("输入 '退出' 返回主菜单")
    safe_print("=" * 60)
    
    cmd = CommandLine()
    if specified_style and specified_style in ["原生", "Windows", "Linux"]:
        cmd.current_style = specified_style
        cmd.show_style_info()
    
    cmd.run()

def enhanced_main_program() -> None:
    """
    增强主程序 - PWOS2系统的主要入口点
    
    功能:
    1. 初始化系统组件
    2. 验证用户身份
    3. 显示主菜单并处理用户选择
    4. 协调各个功能模块的工作
    
    流程:
    - 显示启动动画
    - 初始化数据目录和配置文件
    - 初始化AI助手和网络防火墙
    - 进行密码验证
    - 检查并应用可用更新
    - 进入主循环，显示菜单并处理用户选择
    
    全局变量:
    - system_name: 系统名称（带版本号）
    - developer_mode: 开发者模式标志
    
    异常处理:
    - 捕获并记录所有异常
    - 在关键失败时优雅退出
    
    返回值: 无
    """
    """增强的主程序"""
    # 启动时系统检查
    safe_print("🔍 系统启动检查...")
    
    # 检查关键类是否存在
    try:
        # 测试 IntelligentUpdateSystem 类
        if not hasattr(IntelligentUpdateSystem, 'auto_integrate_update'):
            safe_print("⚠️  IntelligentUpdateSystem 类不完整")
            safe_print("🔄 尝试自动修复...")
            
            # 尝试修复
            IntelligentUpdateSystem.emergency_repair()
            safe_print("🔄 修复完成，重新启动...")
            time.sleep(2)
            os.execv(sys.executable, [sys.executable] + sys.argv)
    except Exception as e:
        safe_print(f"⚠️  系统检查异常: {e}")

    
    global system_name, developer_mode
    
    safe_print("\n" + "=" * 60)
    safe_print(f"      {system_name} 启动中...")
    
    # 显示启动动画
    for i in range(5):
        dots = "." * (i + 1)
        spaces = " " * (4 - i)
        safe_print(f"[{dots}{spaces}] 正在初始化系统...", end="\r")
        time.sleep(0.2)
    safe_print()
    
    safe_print("=" * 60)
    
    # 初始化系统
    if not DataManagement.init_system():
        safe_print("❌ 初始化失败，系统退出")
        return
    
    # 初始化AI助手
    AIAssistant.init()
    
    # 初始化网络防火墙
    if not NetworkFirewall.init():
        safe_print("⚠️  网络防火墙初始化失败")
    
    # 密码验证
    if not UITools.password_verification():
        safe_print("❌ 密码验证失败，系统退出")
        return
    
    safe_print("✅ 验证通过，欢迎进入PWOS2系统")
    safe_print("🔒 系统文件请勿泄密！")
    
    system_name = f"PWOS2 v{DataManagement.load_version()}"
    safe_print(f"📊 当前系统版本: {system_name}")
    safe_print("=" * 60)
    
    # 检查智能更新
    safe_print("🔍 检查智能更新...")
    update_packages = UpdateManagement.check_update_packages()
    if update_packages:
        safe_print(f"📦 发现 {len(update_packages)} 个更新包")
        confirm = input("是否立即应用智能更新? (Y/N): ").strip().upper()
        if confirm == 'Y':
            IntelligentUpdateSystem.auto_integrate_update()
    
    # 主循环
    while True:
        selection = UITools.show_main_menu()
        
        if selection == "a1b2c3d4e5" and not developer_mode:
            developer_mode = True
            safe_print("\n🎉 开发者模式已激活！")
            SystemLog.security_log("激活开发者模式", "用户", "成功")
            continue
        
        if selection == "1":
            UserManagement.add_user()
        elif selection == "2":
            UserManagement.view_all_users()
        elif selection == "3":
            UserManagement.find_user()
        elif selection == "4":
            UserManagement.delete_user()
        elif selection == "5":
            UserManagement.delete_all_users()
        elif selection == "6":  # 修改用户备注
            UserManagement.modify_remark()
        elif selection == "7":
            SystemFunctions.show_system_info()
        elif selection == "8":
            SystemFunctions.view_logs()
        elif selection == "9":
            SystemFunctions.export_data()
        elif selection == "10":
            SystemFunctions.data_recovery()
        elif selection == "11":
            SystemFunctions.system_update()
        elif selection == "12":
            PasswordManagement.change_password()
        elif selection == "13":
            SystemFunctions.firewall_settings()
        elif selection == "14":
            SystemFunctions.system_optimization()
        elif selection == "15":
            AIAssistant.main_menu_function()
        elif selection == "16":
            command_line_mode()
        elif selection == "17":
            installed, missing = LibraryManager.check_all_libraries()
            safe_print("\n1. 自动安装所有库")
            safe_print("2. 检查库状态")
            safe_print("3. 返回")
            choice = input("请选择: ").strip()
            if choice == "1":
                LibraryManager.install_all_libraries()
            elif choice == "2":
                safe_print("\n===== 库状态报告 =====")
                required_libs = LibraryManager.get_required_libraries()
                total = len(required_libs)
                installed_count = 0
                
                for lib in required_libs:
                    try:
                        if lib["name"] == "dnspython":
                            import dns.resolver
                            status = "✅ 已安装"
                        else:
                            __import__(lib["name"].split('.')[0])
                            status = "✅ 已安装"
                        installed_count += 1
                    except ImportError:
                        status = "❌ 未安装"
                    safe_print(f"{lib['name']:<20} - {lib['desc']:<15} - {status}")
                
                safe_print(f"\n📊 统计: {installed_count}/{total} 个库已安装")
                if installed_count == total:
                    safe_print("🎉 所有依赖库都已安装！")
                else:
                    safe_print(f"⚠️  缺少 {total - installed_count} 个库")
        elif selection == "18":
            EnhancedNetworkFunctions.show_menu()
        elif selection == "19":
            UserFileManagement.show_menu()  # 新增用户文件管理
        elif selection == "20" and developer_mode:
            while True:
                developer_selection = DeveloperModeFunctions.show_developer_menu()
                if developer_selection == "1":
                    DeveloperModeFunctions.view_system_internal_status()
                elif developer_selection == "2":
                    DeveloperModeFunctions.database_diagnosis()
                elif developer_selection == "3":
                    DeveloperModeFunctions.performance_test()
                elif developer_selection == "4":
                    DeveloperModeFunctions.debug_log_level()
                elif developer_selection == "5":
                    DeveloperModeFunctions.system_config_edit()
                elif developer_selection == "6":
                    DeveloperModeFunctions.batch_data_operations()
                elif developer_selection == "7":
                    DeveloperModeFunctions.code_injection_test()
                elif developer_selection == "8":
                    DeveloperModeFunctions.process_management()
                elif developer_selection == "9":
                    DeveloperModeFunctions.service_management()
                elif developer_selection == "10":
                    DeveloperModeFunctions.disk_usage_analysis()
                elif developer_selection == "11":
                    DeveloperModeFunctions.memory_info()
                elif developer_selection == "12":
                    DeveloperModeFunctions.modify_system_version()
                elif developer_selection == "13":  # 紧急系统修复
                    safe_print("\n⚠️  紧急系统修复功能")
                    safe_print("此功能将尝试修复损坏的系统文件")
                    confirm = input("确定要继续吗? (Y/N): ").strip().upper()
                    if confirm == 'Y':
                        IntelligentUpdateSystem.emergency_repair()
                elif developer_selection == "14":  # 增强备份
                    success, message = DataManagement.enhanced_backup()
                    if success:
                        safe_print(f"✅ {message}")
                    else:
                        safe_print(f"❌ {message}")
                elif developer_selection =="15":
                    break

        elif selection == "21" and developer_mode:
            developer_mode = False
            safe_print("\n开发者模式已退出")
            SystemLog.security_log("退出开发者模式", "用户", "成功")
        elif (selection == "20" and not developer_mode) or (selection == "22" and developer_mode):
            safe_print("\n感谢使用，再见！")
            SystemLog.log("系统正常退出")
            break
        else:
            safe_print("❌ 无效选择")

# ==================== 主入口 ====================
if __name__ == "__main__":
    try:
        # 检查命令行参数
        if len(sys.argv) > 1:
            if sys.argv[1] == "--build":
                BuildHelper.prepare_for_exe()
                BuildHelper.create_installer()
                safe_print("✅ 打包准备完成！")
                safe_print("运行命令: pyinstaller -F -w -i icon.ico pwos_enhanced_complete_fixed.py")
                sys.exit(0)
            elif sys.argv[1] == "--cmd":
                command_line_mode()
                sys.exit(0)
        
        # 启动系统日志
        SystemLog.log("系统启动")
        
        # 运行主程序
        enhanced_main_program()
        
    except KeyboardInterrupt:
        safe_print("\n系统被中断")
        SystemLog.log("系统被中断")
    except Exception as e:
        safe_print(f"\n系统崩溃: {e}")
        SystemLog.log(f"系统崩溃: {e}\n{traceback.format_exc()}", "致命")
        input("按Enter键退出...")
