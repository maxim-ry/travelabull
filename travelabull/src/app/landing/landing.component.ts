/// <reference types="@types/googlemaps" />

import { Component, OnInit, ViewChild, ElementRef, NgZone } from '@angular/core';
import { FormControl } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

declare var google: any;

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.css']
})
export class LandingComponent implements OnInit {
  
  public startDate: Date = new Date();
  public endDate: Date = new Date();
  public specification: String = "";
  
  public addressControl = new FormControl();
  @ViewChild('search', {static: false}) public searchElementRef!: ElementRef;

  constructor(private ngZone: NgZone,  private http: HttpClient, private router: Router) {}

  ngOnInit() {}

  ngAfterViewInit() {
    this.initAutocomplete();
  }

  private initAutocomplete(): void {
    // Wait for the Google Maps script to be loaded before initializing the autocomplete
    if (typeof google !== 'undefined') {
      const autocomplete = new google.maps.places.Autocomplete(this.searchElementRef.nativeElement, {
        types: ["(regions)"], // or ['geocode'] depending on requirements
      });
      autocomplete.addListener("place_changed", () => {
        this.ngZone.run(() => {
          const place: google.maps.places.PlaceResult = autocomplete.getPlace();
          if (place.geometry) {
            this.addressControl.setValue(place.formatted_address);
          } else {
            console.log('No details available for input: ' + place.name);
          }
        });
      });
    } else {
      console.error('Google maps script not loaded');
    }
  }

  submit() {
    // console.log(this.startDate);
    // console.log(this.endDate);
    // console.log(this.specification);
    // console.log(this.addressControl.value);

    const differenceInMs = this.endDate.getTime() - this.startDate.getTime();
    const differenceInDays = Math.floor(differenceInMs / (1000 * 60 * 60 * 24)) + 1;

    //console.log(differenceInDays);

    // Prepare the data to send to the Flask backend
  const data = {
    startDate: this.startDate,
    endDate: this.endDate,
    specification: this.specification,
    location: this.addressControl.value,
    differenceInDays: differenceInDays
  };

    // Send the data to your Flask API endpoint
    this.http.post('http://127.0.0.1:5000/api/data', data).subscribe(
      (response) => {
        console.log('Data sent successfully:', response);
        // Handle success if needed
      },
      (error) => {
        console.error('Error sending data:', error);
        // Handle error if needed
      }
    );

    this.router.navigate(['/result']);

  
  
}

  

}