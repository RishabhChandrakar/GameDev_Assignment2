def minimax(depth,player,node_index,alpha,beta,array,alpha_list,beta_list):
   
    if depth==0:
        return array[node_index]

    alpha_list[node_index]=alpha
    beta_list[node_index]=beta

    if player:
        
        a=minimax(depth-1,not player,2*node_index+1,alpha_list[node_index],beta_list[node_index],array,alpha_list,beta_list)

        alpha_list[node_index]=max(alpha_list[node_index],a)

        if alpha_list[node_index]>beta_list[node_index]:    #if these become True it means we can prune the 2*nodex+2 part
                
            array[node_index]=a
            alpha_list[int((node_index-1)/2)]=alpha_list[node_index]
            beta_list[int((node_index-1)/2)]=beta_list[node_index]
                
            return array[node_index]
            
        else:
            b=minimax(depth-1,not player,2*node_index+2,alpha_list[node_index],beta_list[node_index],array,alpha_list,beta_list)

            alpha_list[node_index]=max(a,b,alpha_list[node_index])

            array[node_index]=max(a,b)
            
            alpha_list[int((node_index-2)/2)]=alpha_list[node_index]
            beta_list[int((node_index-2)/2)]=beta_list[node_index]
            
            return array[node_index]

            
        
    else:
        a=minimax(depth-1,not player,2*node_index+1,alpha_list[node_index],beta_list[node_index],array,alpha_list,beta_list)

        beta_list[node_index]=min(beta_list[node_index],a)

        if alpha_list[node_index]>beta_list[node_index]:
                
            array[node_index]=a
            
            alpha_list[int((node_index-1)/2)]=alpha_list[node_index]
            beta_list[int((node_index-1)/2)]=beta_list[node_index]
                
            return array[node_index]
            
        else:
            b=minimax(depth-1,not player,2*node_index+2,alpha_list[node_index],beta_list[node_index],array,alpha_list,beta_list)

            beta_list[node_index]=min(a,b,beta_list[node_index])

            array[node_index]=min(a,b)
            
            alpha_list[int((node_index-2)/2)]=alpha_list[node_index]
            beta_list[int((node_index-2)/2)]=beta_list[node_index]
            
            return array[node_index]

    return array[node_index]

list1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,8,6,9,10,5,3,12,3,5,2,9,12,5,23,23]


alpha_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
beta_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

minimax(4,True,0,-1000,1000,list1,alpha_list,beta_list)

print(alpha_list,"\n")
print(beta_list,"\n")

print("evaluation of leaves are : ")
print(list1)
