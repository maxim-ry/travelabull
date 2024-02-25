/// <reference types="@types/googlemaps" />

import { Component, OnInit, ViewChild, ElementRef, NgZone } from '@angular/core';
import { FormControl } from '@angular/forms';

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

  constructor(private ngZone: NgZone) {}

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
    console.log(this.startDate);
    console.log(this.endDate);
    console.log(this.specification);
    console.log(this.addressControl.value);

    const differenceInMs = this.endDate.getTime() - this.startDate.getTime();
    const differenceInDays = Math.floor(differenceInMs / (1000 * 60 * 60 * 24)) + 1;

    console.log(differenceInDays);
  }

}