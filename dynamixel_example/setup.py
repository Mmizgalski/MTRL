def setup():
    # ustawienie limitów pozycji
    min_lim_pos = input("Minimal position from 0 to 4095 (0 is 0 degree 4095 is 360 degree)= ")
    max_lim_pos = input("Maximum position from 0 to 4095 (0 is 0 degree 4095 is 360 degree)= ")
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_PRO_POSITION_MIN_LIMIT, min_lim_pos)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_PRO_POSITION_MAX_LIMIT, max_lim_pos)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    # ustawienie profilu prędkości
    profile_vel = input("Set the profile of velocity from 0 to 32767 ( from 0 to 0.229 [rev/min])= ")
    dxl_comm_result,dxl_error = packetHandle.write1ByteTxRx(portHandler, DXL_ID, ADDR_PRO_VELOCITY_PROFILE, profile_vel)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
        packetHandler.write4ByteTxRx()
    else:
        fprint("Velocity profile set at "+ profile_vel )

    #ustawienie profilu przyspieszenia
    profile_accel = input("Set the profile of acceleration from 0 to 32767 ( from 0 to 214.577 [rev/min^2])= ")
    dxl_comm_result, dxl_error = packetHandle.write1ByteTxRx(portHandler, DXL_ID, ADDR_PRO_ACC_PROFILE , profile_accel)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
        packetHandler.write4ByteTxRx()
    else:
        fprint("Acceleration profile set at " + profile_vel)
    end