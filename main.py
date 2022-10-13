from src.dataproc import DataProcess
from src.lenanalyse import LengthAnalyse
from src.eleanalyse import ElementAnalyse


if __name__ == '__main__':
    data_path = './data/'
    res_path = './result/'

    DataProcess(data_path)
    # LengthAnalyse(data_path, res_path)
    # ElementAnalyse(data_path, res_path)

