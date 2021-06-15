w, b = map(float, input().split())

if w+0.5<=b and w %5==0: b=b-(w+0.5)
print("%.2f" % b)
