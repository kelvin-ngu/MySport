import { Component, Input } from '@angular/core';
import { Postlist } from '../postlist';
import { PostComponent } from '../post/post.component';

@Component({
  selector: 'app-mental-health',
  templateUrl: './mental-health.component.html',
  styleUrls: ['./mental-health.component.css'],
  imports: [PostComponent],
  standalone: true
})
export class MentalHealthComponent {
  @Input() postList!: Postlist;  
}
