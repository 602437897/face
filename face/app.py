import face_test


if __name__ == '__main__':
    filePath = 'last.jpg';
    face_test.get_img(filePath)
    result = face_test.face_match(filePath)
    print result['result'][0]['score']
    if result['result'][0]['score'] >= 80:
        print 1;