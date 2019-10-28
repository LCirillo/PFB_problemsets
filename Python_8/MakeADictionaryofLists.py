df = pd.read_csv('./combined.csv')

master_dict= {}

for i in range(len(df)):
    louvain= (df.loc[i,'louvain'])
    stage= (df.loc[i,'STAGE'])
    xcoor= (df.loc[i,'0'])
    ycoor= (df.loc[i,'1'])
    
    if louvain in testdict:
        stage_list.append(stage) 
        xcoor_list.append(xcoor) 
        ycoor_list.append(ycoor)
    else:
        stage_list= []
        xcoor_list= []
        ycoor_list= []
        master_dict[louvain] = [xcoor_list,ycoor_list,stage_list] 
        stage_list.append(stage) 
        xcoor_list.append(xcoor) 
        ycoor_list.append(ycoor)       
