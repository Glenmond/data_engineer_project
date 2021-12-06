inputs_mappings = {
    "users": f"inputs/users.csv",
    "goals": f"inputs/goals.csv",
    "performance": f"inputs/performance.csv"
}

outputs_mappings = {
    "users": f"users_processed.csv",
    "goals": f"goals_processed.csv",
    "performance": f"performance_processed.csv"
}

goals_col_mappings = {
    "GENERAL_INVESTING": "CORE",
    "RETIREMENT": "CORE",
    "CHILD_EDUCATION": "CORE",
    "BUY_A_HOME": "CORE",
    "EMERGENCY_FUND": "CORE",
    "TRAVEL": "CORE",
    "WEDDING": "CORE",
    "START_BUSINESS": "CORE",
    "VEHICLE": "CORE", 
    "THEME_TECH": "THEMATIC",
    "THEME_CONSUMER": "THEMATIC",
    "THEME_HEALTHCARE": "THEMATIC",
    "INCOME": "INCOME_SGD",
    "MMF": "MMF_SGD",
}