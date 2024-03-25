import cv2
import os

def extract_frames(video_path, output_folder):
    # Tạo thư mục lưu trữ các frame ảnh nếu nó không tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Đọc video
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        
        # Kiểm tra xem có frame tiếp theo hay không
        if not ret:
            break
        
        # Lưu frame ảnh
        frame_count += 1
        frame_name = f"frame_{frame_count:04d}.jpg"
        frame_path = os.path.join(output_folder, frame_name)
        cv2.imwrite(frame_path, frame)

    cap.release()

    print(f"{frame_count} frames have been extracted to {output_folder}.")

if __name__ == "__main__":
    video_path = "tungduong.mp4"  # Thay đổi đường dẫn tới video của bạn
    output_folder = "tungduong_frames"  # Thay đổi tên thư mục đầu ra nếu cần thiết

    extract_frames(video_path, output_folder)
