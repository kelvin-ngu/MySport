import { Component, Input } from '@angular/core';
import { Postlist } from '../postlist';
import { PostComponent } from '../post/post.component';

@Component({
  selector: 'app-physical-care',
  templateUrl: './physical-care.component.html',
  styleUrls: ['./physical-care.component.css'],
  imports: [PostComponent],
  standalone: true
})
export class PhysicalCareComponent {
  @Input() postList!: Postlist;  
}
