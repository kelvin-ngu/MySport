import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PostentryService {
  httpClient: HttpClient  = inject(HttpClient);
  url = 'http://localhost:8000/reflection/journal/';
  constructor() { }

  postEntry(entry: JSON): Observable<any> {
      return this.httpClient.post(this.url, entry);
  }
}
