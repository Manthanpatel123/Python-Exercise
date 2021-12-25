bread={"manthan","bharatbhai","patel"}
butter={"dhruv","mahesbhai","patel"}
milk={"sumit","rajvantbhai","patel"}
print(f"bread buyer {len(bread)}")
print(f"butter buyr {len(butter)}")
print(f"bread and butter buyr {len(bread & butter)}")
print(f"buyr who bought bread but not a butter {bread-butter}")
print(f"buyr who bought all three {bread & butter & milk}")
print(f"the most valuable buyr are {bread & butter & milk}")