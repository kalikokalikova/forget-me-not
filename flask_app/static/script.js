function get_trip_id(element){
    trip_id = element.value;
    document.getElementById('yes-button').href = `/delete_trip/${trip_id}`;
}

let packed_items_list = [];

function change_background(element){
    item_id = element.id;
    this_item = document.getElementById(`${item_id}`);
    if (this_item.className == "selected-for-pack"){
        this_item.className = null;
    }
    else if (this_item.className == "packed"){
        this_item.className == "packed"
    }
    else{
        this_item.className = "selected-for-pack";
        packed_items_list.push(item_id);
    }
    document.getElementById("packed_items_list").value = packed_items_list;
    console.log(document.getElementById("packed_items_list").value);
}