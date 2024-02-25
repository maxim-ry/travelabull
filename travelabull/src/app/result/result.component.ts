// result.component.ts

import { Component } from '@angular/core';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent {
  results = [
    {
      day: 1,
      mapEmbedLink: 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d224055.47027679897!2d-82.45840091274682!3d27.96415767150178!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zN8KwMzEnMTcuMCJOIDgywrAyNy43Ilc!5e0!3m2!1sen!2sus!4v1646212345673!5m2!1sen!2sus',
      schedule: {
        morning: 'Morning Schedule for Day 1',
        afternoon: 'Afternoon Schedule for Day 1',
        evening: 'Evening Schedule for Day 1'
      },
    },{
      day: 1,
      mapEmbedLink: 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2480.846057109642!2d-0.12805638459405855!3d51.50735056491838!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x487603b2f31b9ec9%3A0x5d601e8ee819db1d!2sBig%20Ben!5e0!3m2!1sen!2suk!4v1648705405612!5m2!1sen!2suk',
      schedule: {
        morning: 'Morning Schedule for Day 1',
        afternoon: 'Afternoonasd Schedule for Day 1',
        evening: 'Evening Schedule for Day 1'
      }
    }
    // Add more results as needed
  ];

  constructor() {}
}
