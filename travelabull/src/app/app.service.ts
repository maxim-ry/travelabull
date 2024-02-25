// import { Injectable } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { Observable } from 'rxjs';

// @Injectable({
//   providedIn: 'root',
// })
// export class ApiService {
//   private apiUrl = 'http://127.0.0.1:5000/api/data'; // Adjust the URL

//   constructor(private http: HttpClient) {}

//   getDataFromApi(): Observable<any> {
//     return this.http.get<any>(this.apiUrl);
//   }
// }


// data.service.ts
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private locationSource = new BehaviorSubject<string>('');
  location$ = this.locationSource.asObservable();
  
  
  private differenceInDaysSource = new BehaviorSubject<number>(0);
  differenceInDays$ = this.differenceInDaysSource.asObservable();


  private dataSubject = new BehaviorSubject<any>(null);
  data$ = this.dataSubject.asObservable();

  sendData(data: any): void {
    this.dataSubject.next(data);
  }

  setLocation(location: string) {
    this.locationSource.next(location);
  }

  setDifferenceInDays(differenceInDays: number) {
    this.differenceInDaysSource.next(differenceInDays);
  }
}

