import rclpy
import time


from geometry_msgs.msg import Twist

import sys, select, termios, tty

settings = termios.tcgetattr(sys.stdin)


def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def main(args=None):	

    rclpy.init(args=args)
    node = rclpy.create_node('cmd')
        
    pub = node.create_publisher(Twist, 'cmd', 3)

    speed=0
    angle=0

    
    while True:
        key = getKey()
        if key == "1":
            print(key)
            speed += 100  # 속도를 10 증가시킴
            print(speed)

            # 1번
            twist = Twist()
            speed = float(speed)
            twist.linear.x = speed
            pub.publish(twist)
            time.sleep(10)

            # 180도 회전
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(14)
            
            # 0.5번
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(4)
            
            # 좌측회전
            angle = -45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            # 다시 속도가 50인 상태로 전진
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 0
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            

            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist) 
        
        if key =="2":
            print(key)
            speed += 100  # 속도를 10 증가시킴
            print(speed)

            # 전진 속도를 유지하는 동안 5초간 대기
            twist = Twist()
            speed = float(speed)
            twist.linear.x = speed
            pub.publish(twist)
            time.sleep(16)

            # 90도 오른쪽으로 회전하는 동작 추가
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(14)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(10)
            
            angle = -45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            # 다시 속도가 50인 상태로 전진
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 0.0
            speed = 0
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            

            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)  
            
        if key =="3":
            print(key)
            speed += 100  # 속도를 10 증가시킴
            print(speed)

            # 전진 속도를 유지하는 동안 5초간 대기
            twist = Twist()
            speed = float(speed)
            twist.linear.x = speed
            pub.publish(twist)
            time.sleep(22)

            # 90도 오른쪽으로 회전하는 동작 추가
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(14)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(16)
            
            angle = -45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            # 다시 속도가 50인 상태로 전진
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(4)
            
            angle = 0.0
            speed = 0
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            

            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)    
            
        if key == "4":
            print(key)
            speed += 100  # 속도를 10 증가시킴
            print(speed)

            # 전진 속도를 유지하는 동안 5초간 대기
            twist = Twist()
            speed = float(speed)
            twist.linear.x = speed
            pub.publish(twist)
            time.sleep(11)

            # 90도 오른쪽으로 회전하는 동작 추가
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)

            #180
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(14)

            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)

            angle = -45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)

            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            
            angle = -45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 0.0
            speed = 0
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            

            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)
                
        if key =="5":
            print(key)
            speed += 100  # 속도를 10 증가시킴
            print(speed)

            # 전진 속도를 유지하는 동안 5초간 대기
            twist = Twist()
            speed = float(speed)
            twist.linear.x = speed
            pub.publish(twist)
            time.sleep(17)

            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            # 180도 오른쪽으로 회전하는 동작 추가
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(14)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            
            angle = -45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(10)
            
            angle = -45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            # 다시 속도가 50인 상태로 전진
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            
            angle = 0.0
            speed = 0
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            

            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)
        
        if key =="6":
            print(key)
            speed += 100  # 속도를 10 증가시킴
            print(speed)

            # 전진 속도를 유지하는 동안 5초간 대기
            twist = Twist()
            speed = float(speed)
            twist.linear.x = speed
            pub.publish(twist)
            time.sleep(22)
            
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            
            # 180도 오른쪽으로 회전하는 동작 추가
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(14)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)

            # 90도 오른쪽으로 회전하는 동작 추가
            angle = -45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6.5)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(15)
            
            angle = -45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            # 다시 속도가 50인 상태로 전진
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(3)
            
            angle = 0.0
            speed = 0
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            

            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)
            
        if key == "7":
            print(key)
            speed += 100  # 속도를 10 증가시킴
            print(speed)

            # 전진 속도를 유지하는 동안 5초간 대기
            twist = Twist()
            speed = float(speed)
            twist.linear.x = speed
            pub.publish(twist)
            time.sleep(10)

            # 90도 오른쪽으로 회전하는 동작 추가
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(10)

            #180
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(14)

            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(10)

            angle = -45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)

            # 다시 속도가 50인 상태로 전진
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            
            angle = -45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            
            angle = 0.0
            speed = 0
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            

            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)    
            
        if key =="8":
            print(key)
            speed += 100  # 속도를 10 증가시킴
            print(speed)

            # 전진 속도를 유지하는 동안 5초간 대기
            twist = Twist()
            speed = float(speed)
            twist.linear.x = speed
            pub.publish(twist)
            time.sleep(16)

            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(10)
            
            # 180도 오른쪽으로 회전하는 동작 추가
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(14)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(10)
            
            angle = -45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(10)
            
            angle = -45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            # 다시 속도가 50인 상태로 전진
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            
            angle = 0.0
            speed = 0
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            

            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)    
            
        if key =="9":
            print(key)
            speed += 100  # 속도를 10 증가시킴
            print(speed)

            # 전진 속도를 유지하는 동안 5초간 대기
            twist = Twist()
            speed = float(speed)
            twist.linear.x = speed
            pub.publish(twist)
            time.sleep(22)
            
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(10)
            
            # 180도 오른쪽으로 회전하는 동작 추가
            angle = 45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(15)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(10)

            # 90도 오른쪽으로 회전하는 동작 추가
            angle = -45
            speed = 0.0
            twist = Twist()
            angle = float(angle)
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(8)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(15)
            
            angle = -45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            # 다시 속도가 50인 상태로 전진
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(6)
            
            angle = 45
            speed = 0.0
            angle = float(angle)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(7)
            
            angle = 0.0
            speed = 100
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(3)
            
            angle = 0.0
            speed = 0
            speed = float(speed)
            twist = Twist()
            twist.linear.x = speed
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(5)
            

            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)    
            
        if key =="e":
            print(key)
            angle=0.0
            speed=0.0
            break
        print(1)


#         twist = Twist()
#         speed=float(speed)
#         twist.linear.x = speed; twist.linear.y = 0.0; twist.linear.z = 0.0
#         twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = float(angle)
#         pub.publish(twist)


        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
       
main()
