max_out = -1
def algor(g, p, ig, trav, k):
  global max_out
  if(ig == len(g)):
    if(len(trav) >= max_out):
      max_out = len(trav)
      print(trav)
    return
  t = True
  for i in p:
    if(abs(g[ig]-i) <=k):
      trav_cp = list(trav)
      p_cp = list(p)
      p_cp.remove(i)
      trav_cp.append((g[ig], i))
      algor(g, p_cp, ig+1, trav_cp, k)
  algor(g, p, ig+1, trav, k)
  return
arr = input()
k = int(input())
g = []
p = []
for i in range(len(arr)):
  if(arr[i]=='G'):
    g.append(i)
  else:
    p.append(i)
algor(g, p, 0, [], k)
print(f'score = {max_out}')