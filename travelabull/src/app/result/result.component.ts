import { Component, OnInit } from '@angular/core';
import { DataService } from '../app.service';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {

  public receivedData: any = {"Day 1": {"Morning": [], "Afternoon": [], "Evening": []}};
  
  receivedLocation: string = '';
  receivedDifferenceInDays: number = 0;

  constructor(private dataService: DataService) {}

  ngOnInit() {
    // Subscribe to the shared service to receive the data
    this.dataService.data$.subscribe((data) => {
      this.receivedData = data;
      console.log('Received Data in ResultComponent:', this.receivedData);
    });
    
    this.dataService.location$.subscribe(location => {
      this.receivedLocation = location || ''; // Use an empty string if location is falsy
    });

    this.dataService.differenceInDays$.subscribe(differenceInDays => {
      this.receivedDifferenceInDays = differenceInDays || 0; // Use 0 if differenceInDays is falsy
    });
  }
}