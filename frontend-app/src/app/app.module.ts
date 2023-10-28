import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { CommunityComponent } from './community/community.component';

import { RouterModule } from '@angular/router';

import { MygameComponent } from './mygame/mygame.component';
import { NewEntryComponent } from './new-entry/new-entry.component';
import { EntryboxComponent } from './entrybox/entrybox.component';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    NewEntryComponent,
    EntryboxComponent,
    AppComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot([
      {path: '', component: HomeComponent},
      {path: 'mygame', component: MygameComponent},
      {path: 'mycommunity', component: CommunityComponent}
    ]),
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
