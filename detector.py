def detect_type(user_input):
    user_input = user_input.strip()

    # Boolean detection
    if user_input.lower() in ["true", "false"]:
        return "bool"

    # Integer
    if user_input.isdigit():
        return "int"

    # Float
    try:
        float(user_input)
        if "." in user_input:
            return "float"
    except:
        pass

    # List
    if user_input.startswith("[") and user_input.endswith("]"):
        return "list"

    # Dict
    if user_input.startswith("{") and user_input.endswith("}"):
        return "dict"

    return "str"