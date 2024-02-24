import { Component } from '@angular/core';
import { NgModel } from '@angular/forms';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.css']
})
export class LandingComponent {
  range: { start: Date | null, end: Date | null } = { start: null, end: null };

  submit() {
    // Handle submission logic here
    console.log('Search submitted!');
    console.log('Selected Date Range:', this.range);
  }
}
