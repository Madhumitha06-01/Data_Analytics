import csv
def clean_data (input_file,output_file):
    cleaned_data=[]
# read a data 
    with open ("raw_data.csv",mode="r")as file:
        reader =csv.reader(file)
        header=next(reader)
        cleaned_data.append(header)
        for row in reader:
            if row[1] =='' or row[1]=="Nan" or not row[1].isdigit():
                row[1]="Unknow" # replace a unknow 
            if row[2] =='' or row[2] =="Nan" or not row[2].isdigit():
                row[2]="0" # replace a unknow 
            cleaned_data.append(row)
# write a new data on it 
    with open (output_file,mode='w',newline='')as file:
        writer=csv.writer(file)
        writer.writerows(cleaned_data)
    print(f"cleaned data is saved at {output_file}")

clean_data("raw_data.csv","raw_data1.csv")