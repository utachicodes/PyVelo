try:
    import pyvelo
    print(f"Success: {pyvelo.__file__}")
except Exception as e:
    print(f"Error: {e}")
