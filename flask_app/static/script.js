function get_trip_id(element){
    trip_id = element.value
    document.getElementById('yes-button').href = `/delete_trip/${trip_id}`
}