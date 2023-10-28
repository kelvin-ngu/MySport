import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CreatepostService {
  httpClient: HttpClient  = inject(HttpClient);
  url = 'http://localhost:8000/forum/post/';
  constructor() {}
  postPost(post: JSON): Observable<any>{
    return this.httpClient.post(this.url, post);
  }
}
