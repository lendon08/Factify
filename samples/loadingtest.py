# import itertools
# import threading
# import time
# import sys
# done = False
# #here is the animation
# def animate():
#     for c in itertools.cycle(['|', '/', '-', '\\']):
#         if done:
#             break
#         sys.stdout.write('\rloading ' + c)
#         sys.stdout.flush()
#         time.sleep(0.1)
#     sys.stdout.write('\rDone!')
# t = threading.Thread(target=animate)
# t.start()
# #long process here
# time.sleep(10)
# done = True

# import time
# # Sleep function
# sleep = time.sleep
# print('L')
# sleep(1)
# print('o')
# sleep(1)  # Sleep 1 second
# print('a')
# sleep(1)
# print('d')
# sleep(1)
# sleep(1)
# print('i')
# sleep(1)
# print('n')
# sleep(1)
# print('g')

# import time
# import sys
# animation = "|/-\\"
# for i in range(20):
#     time.sleep(0.1)
#     sys.stdout.write("\r" + animation[i % len(animation)])
#     sys.stdout.flush()
#     print('Loading')
# print("\nDone!")

# import time
# import sys
# print("Loading:")
# #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
# animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
# for i in range(len(animation)):
#     time.sleep(1)
#     sys.stdout.write("\r" + animation[i % len(animation)])
#     sys.stdout.flush()
# print("\n")