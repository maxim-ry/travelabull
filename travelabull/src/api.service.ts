// api.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:5000/api/data'; // Adjust the URL

  constructor(private http: HttpClient) {}

  getDataFromApi(): Observable<any> {
    return this.http.post<any>(this.apiUrl, { /* your request data here */ });
  }
}
