def analyze_fuse(current, max_current):
    if current > max_current:
        return "Fuse blown"
    return "Circuit stable"

current = 25
max_current = 20
status = analyze_fuse(current, max_current)
print(status)
