# kamera_yemek.py
import cv2
from ultralytics import YOLO

# Eğittiğin modelin yolu (sonra kendi modelini buraya koyacaksın)
# model = YOLO('yolov8_model/best.pt')
model = YOLO('yolov8_model/best.pt')

# model = YOLO('yolov8n.pt')  # Küçük hazır model, ultralytics paketinden gelir


def yemek_tanima():
    cap = cv2.VideoCapture(0)  # Kamerayı aç

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Model ile tahmin yap
        results = model(frame)

        # Sonuçları çiz (kutular, etiketler)
        for result in results:
            boxes = result.boxes.xyxy
            confidences = result.boxes.conf
            classes = result.boxes.cls

            for i, box in enumerate(boxes):
                x1, y1, x2, y2 = map(int, box)
                conf = confidences[i]
                cls = int(classes[i])
                label = model.names[cls]

                # Kutu çiz
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                # Etiket yaz
                cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        cv2.imshow('Yemek Tanıma', frame)

        # q ile çıkış
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    yemek_tanima()
