while True:
    weight = float(input())
    if weight == -1:
        break
    print(
        f"Objects weighing {weight:.2f} on Earth will weigh {weight * 0.167:.2f} on the moon."
    )
