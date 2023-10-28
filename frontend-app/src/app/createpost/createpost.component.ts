import { Component, inject } from '@angular/core';
import { CreatepostService } from '../createpost.service';

@Component({
  selector: 'app-createpost',
  templateUrl: './createpost.component.html',
  styleUrls: ['./createpost.component.css'],
  standalone: true
})
export class CreatepostComponent {
  content = "What's on your mind?";
  title = "Title";
  createPostService: CreatepostService = inject(CreatepostService);
  postPost(title: string, content: string) {
    const jsonPost = <JSON><unknown>{ category: "PHYSICAL_CARE",
      title: title,
      description: content,
      author: "c0b4902b-4007-4cfc-838c-07fa4820cc15"
    }
    this.createPostService.postPost(jsonPost).subscribe((response) => {
      console.log(response);
      this.content = "What's on your mind?";
      this.title = "Title";
    })

  }
  
}