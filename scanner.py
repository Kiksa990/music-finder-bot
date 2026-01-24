import risk_engine

def scan_lite(user_id: int, file_path: str) -> str:
    result = risk_engine.check_file(file_path, mode="lite")
    return f"👤 Пользователь {user_id}\n{result}"

def scan_deep(user_id: int, file_path: str) -> str:
    result = risk_engine.check_file(file_path, mode="deep")
    return f"👤 Пользователь {user_id}\n{result}"

def scan_basic(user_id: int, file_path: str) -> str:
    result = risk_engine.check_file(file_path, mode="basic")
    return f"👤 Пользователь {user_id}\n{result}"

def scan_pro(user_id: int, file_path: str) -> str:
    result = risk_engine.check_file(file_path, mode="pro")
    return f"👤 Пользователь {user_id}\n{result}"