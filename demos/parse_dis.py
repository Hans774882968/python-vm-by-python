global_demo_path = 'demos/comprehensive_demo1_g'
with open(f'{global_demo_path}.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()[2:]
    ans = []
    for line in lines:
        a = line.strip().split(' ')
        tmp = []
        for v in a:
            if v:
                tmp.append(v)
        a = tmp
        for i, s in enumerate(a):
            if not s[0].isalpha():
                continue
            ans.append((s,) if i == len(a) - 1 else (s, int(a[i + 1])))
            break
    for v in ans:
        print(str(v) + ",")
