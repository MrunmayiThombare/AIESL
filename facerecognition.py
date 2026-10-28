import face_recognition

known = face_recognition.load_image_file("known.png")
unknown = face_recognition.load_image_file("test.png")

k = face_recognition.face_encodings(known)[0]
u = face_recognition.face_encodings(unknown)[0]

if face_recognition.compare_faces([k], u)[0]:
    print("Face matched!")
else:
    print("Face not matched!")
