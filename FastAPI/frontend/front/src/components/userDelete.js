import axios from "axios";
import React from "react";

function UserItems(props){

    const deleteListhandler =(name)=> {
        axios.get('http://localhost:8000/formdata/${name}')
        .then(res=>
          console.log(res)
        )
      };  
      
        return(
            <>
            <div> 
            <P>

               <span style={{fontWeight:"bold"}}> {props.formdata.name}</span> 
               {props.todo.city}

                <button onClick={()=>deleteListhandler(props.formdata.name)}>  X</button>

            </P>
            </div>
            </>

        )

}


export default UserItems;








