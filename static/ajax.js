"use strict."

    

function showAllEvents (evt) {

    evt.preventDefault();

    $.get('/all_events', (res) => {

        for (event of res) {
            $('#DataResults').append(
                `<a href="#" class="list-group-item list-group-item-action">
                <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">${event.type} - ${event.location}</h5>
                </div>
                <p class="mb-1">${event.weekday} at ${event.time}</p>
                </a>`
            );
        }
    });
}

$('#viewAllEvents').on('click', showAllEvents);







function showAllLocations (evt) {

    evt.preventDefault();

    $.get('/all_locations', (res) => {

        for (location of res) {
            $('#DataResults').append(
                `<a href="#" class="list-group-item list-group-item-action">
                <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">${location.name}</h5>
                </div>
                <p class="mb-1">${location.address}</p>
                <p class="mb-1">${location.city}, MN ${location.zipcode}
                </p></a>`
            );
        }
    });
}

$('#viewAllLocations').on('click', showAllLocations);



// $(function() {
//     $('#viewAllEvents').on('click', showAllEvents);

//     function showAllEvents (evt) {

//         evt.preventDefault();
    
//         $.get('/all_events', (res) => {

//             for (event of res) {
//                 $('#DataResults').append(
//                     `<a href="#" class="list-group-item list-group-item-action">
//                     <div class="d-flex w-100 justify-content-between">
//                     <h5 class="mb-1">${event.type} - ${event.location}</h5>
//                     </div>
//                     <p class="mb-1">${event.weekday} at ${event.time}</p>
//                     </a>`
//                 );
//             }
//         });
//     }

// })


// $(function() {
//     $('#viewAllLocations').on('click', showAllLocations);

//     function showAllLocations (evt) {

//         evt.preventDefault();
    
//         $.get('/all_locations', (res) => {

//             for (location of res) {
//                 $('#DataResults').append(
//                     `<a href="#" class="list-group-item list-group-item-action">
//                     <div class="d-flex w-100 justify-content-between">
//                     <h5 class="mb-1">${location.name}</h5>
//                     </div>
//                     <p class="mb-1">${location.address}</p>
//                     <p class="mb-1">${location.city}, MN ${location.zipcode}
//                     </p></a>`
//                 );
//             }
//         });
//     }

// })


