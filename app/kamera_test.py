import cv2

def kamera_ac():
    cap = cv2.VideoCapture(0)  # 0 = default kamera

    if not cap.isOpened():
        print("Kamera açılamadı!")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kare alınamadı, çıkılıyor.")
            break
        
        cv2.imshow('Kamera Görüntüsü', frame)

        # 'q' tuşuna basınca çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    kamera_ac()
