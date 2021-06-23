import iftv
import argparse
import datetime
import time

def main():
    # params list
    binLen = 2000
    treeNum = 256
    treeSampleNum = 256
    alpha = 0.25
    threshold = 0.01

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', help='bam file path')
    parser.add_argument('-r', help='reference file path')
    parser.add_argument('-o', help='output label, preferably just put the sample name here')

    parameters = parser.parse_args()
    # rdName = "CR611.final.bam"
    # chrFile = "/Volumes/workstuff/hg38.analysisSet/hg38.analysisSet.fa"
    chrFile = parameters.r
    # rdFile = "/Volumes/Eve_SSD/WES/Novogene_WES_2021May27/02.Bam/" + rdName
    rdFile = parameters.b
    outputFile = parameters.o+".txt" 
    statisticFile = "statistic_10x_change"+parameters.o+".txt"
    calculateFile = "calculateFile_abCN"+parameters.o+".txt"
    beforeFile = "beforefile_CN"+parameters.o+".txt"

    params = (binLen, chrFile, rdFile, outputFile, statisticFile, treeNum, treeSampleNum, alpha, threshold, calculateFile , beforeFile)
    iftv.main(params)


if __name__ == "__main__":
    start_time = time.time()
    print(datetime.datetime.now()+'\n')
    main()
    print(datetime.datetime.now()+'\n')
    print(" %s seconds " % (time.time() - start_time))