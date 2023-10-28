import { Component, inject } from '@angular/core';
import { PostentryService } from '../postentry.service';

@Component({
  selector: 'app-entrybox',
  templateUrl: './entrybox.component.html',
  styleUrls: ['./entrybox.component.css'],
  standalone: true
})
export class EntryboxComponent {
  postEntryService: PostentryService = inject(PostentryService);
  postEntry(title: string, get_up: string, feelings:string, entry: string) {
    const jsonEntry = <JSON><unknown>{
      title: title,
      get_up: get_up,
      feelings: feelings,
      entry: entry,
      author:"c0b4902b-4007-4cfc-838c-07fa4820cc15",
    }
    this.postEntryService.postEntry(jsonEntry).subscribe((response) => {
      console.log(response);
    })
  }
}
