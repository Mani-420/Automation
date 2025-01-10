import time
# print(time.gmtime(0))


# Current time since epoch in seconds----------------------------------
current_time_in_seconds = time.time()
# print("Current time in seconds since epoch =", current_time_in_seconds)


# Current time since epoch in seconds----------------------------------
current_time_till_now = time.ctime()
# print("Current time:", current_time_till_now)


# Delay Execution----------------------------------
# for i in range(4):
#     time.sleep(1)
#     print(i)


# Local Time From epoch----------------------------------
obj = time.localtime()
# print(obj)


# Local Time in Seconds----------------------------------
obj1 = time.gmtime()
time_sec = time.mktime(obj1)
# print("Local time (in seconds):", time_sec)


# Seconds to time.struct_time object----------------------------------
obj2 = time.gmtime()
# print(obj2)


# Seconds to time.struct_time object----------------------------------
