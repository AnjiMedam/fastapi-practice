import UserItems from "./userDelete";

function ListView(props){
    return(
<div>

            <ul>

             {props.useList.map(formdata=><UserItems formdata={formdata} />)}
            </ul>


</div>

    )
}



export default ListView;


