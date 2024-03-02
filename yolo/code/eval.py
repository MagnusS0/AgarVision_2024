from ultralytics import YOLO
import pandas as pd
import os
def main():
    # Load model
    model = YOLO('./runs/detect/train16/weights/best.pt')

    # Evaluate
    results = model.predict('../processed/test/images', stream=True, conf=0.25) 
    evaluate = []
    # evaluate_conf_5 = []
    for result in results:
        # get the image name
        path = result.path
        pic_num = path.split('/')[-1].split('.')[0]
        evaluate.append([pic_num, result.boxes.cls.shape[0]])
        # save the result
        if not os.path.exists('test'):
            os.makedirs('test')
        try:
            result.save(os.path.join('test', pic_num + '.jpg'))
        except:
            print(pic_num)
            continue

    # save the result to csv
    evaluate = pd.DataFrame(evaluate, columns=['ID', 'TARGET'])
    evaluate.to_csv('../processed/test_16_cf_0_2_5.csv', index=False)
if __name__ == '__main__':
    main()
        
